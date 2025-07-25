Name:		python-pyserial
Version:	3.5
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pyserial/pyserial-%{version}.tar.gz
Summary:	Python Serial Port Extension
URL:		https://pypi.org/project/pyserial/
License:	BSD
Group:		Development/Python

Requires:   python%{pyver}dist(setuptools)
BuildSystem:	python

BuildArch:	noarch

%description
Python Serial Port Extension

%files
%{py_sitedir}/serial
%{py_sitedir}/pyserial-*.*-info
%{_bindir}/pyserial-miniterm
%{_bindir}/pyserial-ports
