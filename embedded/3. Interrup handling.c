#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/interrupt.h>
#include <linux/init.h>

#define IRQ_NUM 1   // example IRQ (keyboard IRQ in many systems)

static int irq = IRQ_NUM;

/* Interrupt handler */
static irqreturn_t my_irq_handler(int irq, void *dev_id)
{
    printk(KERN_INFO "Interrupt occurred! IRQ = %d\n", irq);
    return IRQ_HANDLED;
}

/* Module init */
static int __init my_init(void)
{
    int result;

    printk(KERN_INFO "Registering IRQ handler...\n");

    result = request_irq(irq,                                                                   //request_irq() =Registers interrupt handler
                         my_irq_handler,                                                        // irq → interrupt number, my_irq_handler → ISR function,  Runs when interrupt occurs
                         IRQF_SHARED,                                                           // IRQF_SHARED → allows sharing IRQ
                         "my_irq_device",                                                       // name → device name
                         (void *)(my_irq_handler));                                            

    if (result) {
        printk(KERN_ERR "Cannot register IRQ\n");
        return result;
    }

    printk(KERN_INFO "IRQ registered successfully\n");
    return 0;
}

/* Module exit */
static void __exit my_exit(void)
{
    printk(KERN_INFO "Freeing IRQ\n");
    free_irq(irq, (void *)(my_irq_handler));
}

module_init(my_init);
module_exit(my_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Example");
MODULE_DESCRIPTION("Basic Interrupt Handler Driver");
