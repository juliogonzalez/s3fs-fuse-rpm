s3fs-fuse
=========

[![Build Status](https://jenkins.juliogonzalez.es/job/s3fs-fuse-rpm-build/badge/icon)](https://jenkins.juliogonzalez.es/job/s3fs-fuse-rpm-build/)

CentOS/RH/Amazon RPMs for S3FS-Fuse <https://github.com/s3fs-fuse/s3fs-fuse>

Based off the [spec file](http://kad.fedorapeople.org/packages/s3fs/s3fs.spec) created by [Jorge A Gallegos](http://kad.fedorapeople.org/), referenced at <https://bugzilla.redhat.com/show_bug.cgi?id=725292>, and upgraded by [Corey Gilmore](https://github.com/cfg), refered at <https://github.com/cfg/s3fs>

Includes scripts to create RPMs for fuse-2.8.5 if needed.

Tested on x64 CentOS 6.9, CentOS 7.3 and Amazon Linux 2017.03


Build Requirements
------------------

All cases:

* automake
* make
* git
* curl
* rpm-build

fuse 2.85 (if you need to compile it):

* kernel-devel packages (or kernel source) installed that is the SAME version of your running kernel
* gcc
* libselinux-devel
* libtool
* gettext-devel

s3fs:

* fuse-devel (>= 2.8.4, from your distribution, or from this repository)
* gcc-c++
* libcurl-devel
* libxml2-devel
* openssl-devel


Building fresh RPMs
-------------------

Clone the repo:

    git@github.com:juliogonzalez/s3fs-fuse-rpm.git
    cd s3fs-fuse-rpm


Build fuse-2.8.5 RPMs
---------------------

**WARNING**: Because fuse developers migrated from SourceForge to GitHub and deleted all content from SourceForge, the script and the SPEC to build fuse will not work before commit **daf3c1f**. If you are trying to build an old s3fs version (1.79 or older), please build fuse using commit **daf3c1f** or newer.

If you do not have fuse >= 2.8.4 available (which for example is the case for CentOS 6.x), then you may compile 2.8.5 using my fork of [fuse-2.8.5-99.vitki.01.el5.src.rpm](http://rpm.vitki.net/pub/centos/6/source/fuse-2.8.5-99.vitki.01.el5.src.rpm).

Otherwise, you do not need this step, but install fuse-devel and fuse-libs for your system.

Rebuild:

    ./fuse-rpm

And install

    rpm -Uvh RPMS/$HOSTTYPE/fuse-2.8.5-99.vitki.03.*.$HOSTTYPE.rpm RPMS/$HOSTTYPE/fuse-devel-2.8.5-99.vitki.03.*.$HOSTTYPE.rpm RPMS/$HOSTTYPE/fuse-libs-2.8.5-99.vitki.03.*.$HOSTTYPE.rpm


Build the s3fs-fuse RPMs
------------------------

Build the RPMs:

    ./s3fs-build-rpm

And install:

    rpm -Uvh RPMS/$HOSTTYPE/s3fs-fuse-1.84-2.*.$HOSTTYPE.rpm
