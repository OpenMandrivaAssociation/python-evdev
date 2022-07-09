%define module evdev

Name:		python-%{module}
Version:	1.5.0
Release:	1
Summary:	Python 3 bindings to the Linux input handling subsystem
Group:		Development/Python
License:	BSD
URL:		http://python-evdev.rtfd.org
Source0:	https://github.com/gvalkov/python-evdev/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python3egg(setuptools)

%description
This package provides bindings to the generic input event interface in Linux.
The evdev interface serves the purpose of passing events generated in the
kernel directly to userspace through character devices that are typically
located in /dev/input/.

This package also comes with bindings to uinput, the userspace input
subsystem. Uinput allows userspace programs to create and handle input
devices that can inject events directly into the input subsystem.

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

%files
%doc README.rst
%dir %{python_sitearch}/%{module}
%{python_sitearch}/%{module}/*
%{python_sitearch}/%{module}-%{version}-py*.egg-info/
