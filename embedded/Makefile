#################basic########################################
obj-m += hello.o                                      //obj-m → list of modules to build, +means append
                                                      //eg. obj-m += hello.o
                                                      //    obj-m += driver.o    both modules will be build, => hello.ko, driver.ko
  
                                                      //hello.c -> (compile) -> hello.o -> (module linking by Kbuild) -> hello.ko

                                                      // How does compiler know to create .ko? ->Because of Kbuild rules, not your Makefile alone. 
                                                      //When you run: "make -C /lib/modules/$(uname -r)/build M=$(PWD) modules"
                                                      //👉 You are invoking the Linux kernel build system, not normal gcc.
all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules    //👉 You are not compiling directly, You are delegating compilation to the Linux kernel build system (Kbuild)
                                                                   //👉 -C = change directory to "/lib/modules/$(uname -r)/build", points to Kernel build directory (headers + Makefiles)
                                                                   //👉  M= tells kernel: “My module source code is in this directory”
clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean      // modules= Convert source code → loadable kernel module (.ko)
                                                                   // clean = Deletes all generated files, removes .o, .ko, .mod.c,i temp files
