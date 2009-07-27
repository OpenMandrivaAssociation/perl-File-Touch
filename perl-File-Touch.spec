%define upstream_name       File-Touch
%define upstream_version    0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Update access and modification timestamps
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This modules update access and modification timestamps, creating nonexistent
files where necessary.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
# remove left-over files from macosx
rm -f ._*
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc MANIFEST Changes
%{perl_vendorlib}/File
%{_mandir}/*/*

