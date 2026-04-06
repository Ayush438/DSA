//1. Kernel Driver (IOCTL Implementation)
#include <linux/module.h>
#include <linux/fs.h>
#include <linux/cdev.h>
#include <linux/uaccess.h>
#include <linux/ioctl.h>

#define DEVICE_NAME "myioctl"
#define CLASS_NAME  "myclass"

/* 🔥 Magic Number */
#define MY_MAGIC 'K'

/* 🔥 IOCTL Commands */
#define LED_ON      _IO(MY_MAGIC, 1)
#define LED_OFF     _IO(MY_MAGIC, 2)
#define LED_STATUS  _IOR(MY_MAGIC, 3, int)

/* device variables */
static dev_t dev_num;
static struct cdev my_cdev;
static int led_state = 0; // 0=OFF, 1=ON

/* open */
static int my_open(struct inode *inode, struct file *file)
{
    printk(KERN_INFO "Device opened\n");
    return 0;
}

/* ioctl */
static long my_ioctl(struct file *file, unsigned int cmd, unsigned long arg)
{
    int status;

    /* 🔥 Validate magic number */
    if (_IOC_TYPE(cmd) != MY_MAGIC) {
        printk(KERN_INFO "Invalid magic number\n");
        return -EINVAL;
    }

    switch (cmd) {

        case LED_ON:
            led_state = 1;
            printk(KERN_INFO "LED ON\n");
            break;

        case LED_OFF:
            led_state = 0;
            printk(KERN_INFO "LED OFF\n");
            break;

        case LED_STATUS:
            status = led_state;
            copy_to_user((int __user *)arg, &status, sizeof(status));
            printk(KERN_INFO "LED STATUS sent to user\n");
            break;

        default:
            return -EINVAL;
    }

    return 0;
}

/* file operations */
static struct file_operations fops = {
    .owner = THIS_MODULE,
    .open = my_open,
    .unlocked_ioctl = my_ioctl,
};

/* init */
static int __init my_init(void)
{
    alloc_chrdev_region(&dev_num, 0, 1, DEVICE_NAME);

    cdev_init(&my_cdev, &fops);
    cdev_add(&my_cdev, dev_num, 1);

    printk(KERN_INFO "Driver loaded: Major=%d\n", MAJOR(dev_num));
    return 0;
}

/* exit */
static void __exit my_exit(void)
{
    cdev_del(&my_cdev);
    unregister_chrdev_region(dev_num, 1);
    printk(KERN_INFO "Driver unloaded\n");
}

module_init(my_init);
module_exit(my_exit);

MODULE_LICENSE("GPL");

//------------------------------------------------------------------------------------

//2. User Space Program

#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#define MY_MAGIC 'K'

#define LED_ON      _IO(MY_MAGIC, 1)
#define LED_OFF     _IO(MY_MAGIC, 2)
#define LED_STATUS  _IOR(MY_MAGIC, 3, int)

int main()
{
    int fd;
    int status;

    fd = open("/dev/myioctl", O_RDWR);

    if (fd < 0) {
        perror("open failed");
        return -1;
    }

    /* Turn LED ON */
    ioctl(fd, LED_ON);

    /* Get LED status */
    ioctl(fd, LED_STATUS, &status);
    printf("LED status = %d\n", status);

    /* Turn LED OFF */
    ioctl(fd, LED_OFF);

    close(fd);
    return 0;
}

/*
User App
   |
   | ioctl(fd, LED_ON)
   ↓
Kernel VFS
   ↓
file_operations.unlocked_ioctl
   ↓
Driver checks magic number ('K')
   ↓
Switch(cmd)
   ↓
LED ON action executed*/
