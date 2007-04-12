%define	module	File-Touch
%define	name	perl-%{module}
%define	version	0.01
%define	release	2mdk

Summary:	File::Touch 
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://www.cpan.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot/
Buildrequires:	perl-devel
Requires:	perl 
Buildarch:	noarch

%description
File::Touch 

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


