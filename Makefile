

all: stack-vm sasm

.PHONY: stack-vm sasm

stack-vm:
	$(MAKE) -C stack-vm

sasm:
	$(MAKE) -C sasm

clean:
	$(MAKE) -C stack-vm clean
	$(MAKE) -C sasm clean
