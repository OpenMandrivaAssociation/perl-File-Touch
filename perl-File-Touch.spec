%define upstream_name       File-Touch
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Update access and modification timestamps

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This modules update access and modification timestamps, creating nonexistent
files where necessary.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
# remove left-over files from macosx
rm -f ._*
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files 
%doc MANIFEST Changes
%{perl_vendorlib}/File
%{_mandir}/*/*


