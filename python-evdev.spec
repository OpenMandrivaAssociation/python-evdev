%define module evdev

Name:		python-evdev
Version:	1.9.3
Release:	1
Summary:	Python 3 bindings to the Linux input handling subsystem
Group:		Development/Python
License:	BSD-3-Clause
URL:		https://python-evdev.rtfd.org
#Source0:	https://files.pythonhosted.org/packages/source/e/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:	https://github.com/gvalkov/python-evdev/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
This package provides bindings to the generic input event interface in Linux.
The evdev interface serves the purpose of passing events generated in the
kernel directly to userspace through character devices that are typically
located in /dev/input/.

This package also comes with bindings to uinput, the userspace input
subsystem. Uinput allows userspace programs to create and handle input
devices that can inject events directly into the input subsystem.

%files
%doc README.md
%license LICENSE
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
