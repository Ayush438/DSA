//What is cdev? =cdev is a kernel structure that links your driver to a device file (/dev/...) so user programs can interact with it.
//cdev is used to register a character device with the kernel and connect device file operations (open, read, write) to the driver implementation.

#include <linux/module.h>
#include <linux/fs.h>
#include <linux/cdev.h>
#include <linux/uaccess.h>

#define DEVICE_NAME "mychar"
#define BUF_SIZE 1024

static dev_t dev_num;
static struct cdev my_cdev;        //The structure is already defined inside the Linux kernel, not by you.  #include <linux/cdev.h>

static char buffer[BUF_SIZE];

// ---------------- FILE OPERATIONS ----------------

static int my_open(struct inode *inode, struct file *file) {
    printk("Device opened\n");
    return 0;
}

static int my_release(struct inode *inode, struct file *file) {
    printk("Device closed\n");
    return 0;
}

static ssize_t my_read(struct file *file, char __user *user_buf, size_t len, loff_t *offset) {
    copy_to_user(user_buf, buffer, BUF_SIZE);
    printk("Data read\n");
    return BUF_SIZE;
}

static ssize_t my_write(struct file *file, const char __user *user_buf, size_t len, loff_t *offset) {
    copy_from_user(buffer, user_buf, len);
    printk("Data written\n");
    return len;
}

// ---------------- FILE OPERATIONS STRUCT ----------------

static struct file_operations fops = {
    .owner = THIS_MODULE,
    .open = my_open,
    .release = my_release,
    .read = my_read,
    .write = my_write,
};

// ---------------- INIT & EXIT ----------------

static int __init my_init(void) {

    // Allocate device number
    alloc_chrdev_region(&dev_num, 0, 1, DEVICE_NAME);

    // Initialize cdev
    cdev_init(&my_cdev, &fops);

    // Add to kernel
    cdev_add(&my_cdev, dev_num, 1);              //Registers your character device (cdev) with the kernel so it can handle operations for a given device number.

    printk("Driver loaded\n");
    return 0;
}

static void __exit my_exit(void) {

    cdev_del(&my_cdev);
    unregister_chrdev_region(dev_num, 1);

    printk("Driver unloaded\n");
}

module_init(my_init);
module_exit(my_exit);

MODULE_LICENSE("GPL");
--------------------------------------------------------------------------------------
obj-m += mychar.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
--------------------------------------------------------------------------------
//Run steps
1. build //make
2. insert module  //sudo insmod mychar.ko
3. check logs  //dmesg
4. create device file  //sudo mknod /dev/mychar c <major> 0
5. give permission   //sudo chmod 666 /dev/mychar
6. test   //echo "hello" > /dev/mychar
          // cat /dev/mychar

--------------------------------------------------------------------------------------

//alloc_chrdev_region() cdev_init() cdev_add() - Registers the device inside kernel only
//                                                Kernel knows device ✔
//                                                User space does NOT see it ❌
//       class_create() → creates a device class (category)
//        device_create() → creates an actual device entry (/dev/...)
