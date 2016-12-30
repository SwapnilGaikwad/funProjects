

all: stack-vm sasm

.PHONY: stack-vm sasm

stack-vm:
	$(MAKE) -C stack-vm

sasm:
	$(MAKE) -C sasm

test: stack-vm sasm
	cd ./sasm && ./sasm test.sasm
	mv ./sasm/out.bin ./stack-vm
	cd ./stack-vm && ./stack-vm out.bin

clean:
	$(MAKE) -C stack-vm clean
	$(MAKE) -C sasm clean
