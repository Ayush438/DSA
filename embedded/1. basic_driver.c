#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Ayush");
MODULE_DESCRIPTION("Hello World Driver");

static int __init hello_init(void)                                // __init =Marks a function as used only during module loading
{                                                                 //🔥 What happens internally?  when you do: "insmod hello.ko" 
                                                                  //  After execution:👉 Kernel frees this memory 
    printk(KERN_INFO "Hello World: Driver Loaded\n");
    return 0;
}

static void __exit hello_exit(void)                               // __exit =Marks a function as used only during module removal
{
    printk(KERN_INFO "Hello World: Driver Unloaded\n");
}

module_init(hello_init);
module_exit(hello_exit);
