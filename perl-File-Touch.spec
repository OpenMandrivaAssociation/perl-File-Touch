%define	module	File-Touch
%define	name	perl-%{module}
%define	version	0.02
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Update access and modification timestamps
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel
Buildarch:	noarch

%description
This modules update access and modification timestamps, creating nonexistent
files where necessary.

%prep
%setup -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc MANIFEST Changes
%dir %{perl_vendorlib}/File
%{perl_vendorlib}/File/*
%{_mandir}/*/*


