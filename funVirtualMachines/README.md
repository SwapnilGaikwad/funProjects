# funVirtualMachine
Virtual machine created for fun by following a tutorial at https://www.youtube.com/watch?v=BNXP0w4Ppto

##Building the source
cd funVirtualMachine
make

##Test the code
make test

# funPypyVM
Based on https://www.youtube.com/watch?v=5U__sbjazPc

##Building pypy
http://doc.pypy.org/en/latest/build.html

hg clone http://bitbucket.org/pypy/pypy pypy
hg up -r d02b1ad322c6  //This is the latest version being used "changeset: 89281:d02b1ad322c6"

cd pypy/pypy/goal

apt-get install gcc make libffi-dev pkg-config libz-dev libbz2-dev libsqlite3-dev libncurses-dev libexpat1-dev libssl-dev libgdbm-dev tk-dev libgc-dev

python ../../rpython/bin/rpython --opt=2

Above command built 'pypy-c', a binary executable for pypy.

ln -s pypy-c  pypy

cd <project_dir>/funVirtualMachine/funPypyVM
ln -s /home/sgaikwad/softwares/pypy/rpython rpython
ln -s /home/sgaikwad/softwares/pypy/rpython/bin/rpython r

Create vm for hello world program
export PATH=$PATH:<pypy_dir>/pypy/pypy/goal  //Add pypy executable in the PATH
./r vm.py
Above command created a 'vm-c' executable which is executed using,
./vm-c 
