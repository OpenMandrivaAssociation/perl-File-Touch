%define upstream_name       File-Touch
%define upstream_version    0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Update access and modification timestamps
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
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

%changelog
* Mon Jul 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 400641
- update to 0.08
- fixed license field

* Sun Jul 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 400257
- new version

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.06-1mdv2010.0
+ Revision: 374458
- update to 0.06

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.02-3mdv2009.0
+ Revision: 241220
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2008.0
+ Revision: 48162
- new version


* Thu Jan 29 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.01-2mdk
- bzip2

* Wed Jan 28 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.01-1mdk
- from Robin Rosenberg <robin.rosenberg@dewire.com> : 
	- initial contrib import. Needed for building Captive-NTFS

