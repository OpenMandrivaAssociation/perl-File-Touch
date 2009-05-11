%define	module	File-Touch
%define	name	perl-%{module}
%define	version	0.06
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Update access and modification timestamps
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.gz
Buildrequires:	perl-devel
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This modules update access and modification timestamps, creating nonexistent
files where necessary.

%prep
%setup -n %{module}-%{version}

%build
# remove left-over files from macosx
rm ._*
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
#make test

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


