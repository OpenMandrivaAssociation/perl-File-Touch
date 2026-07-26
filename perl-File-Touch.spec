%define upstream_name       File-Touch
Name:		perl-%{upstream_name}
Version:	0.09
Release:	4

Summary:	Update access and modification timestamps

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This modules update access and modification timestamps, creating nonexistent
files where necessary.

%prep
%setup -q -n %{upstream_name}-%{version} 

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


