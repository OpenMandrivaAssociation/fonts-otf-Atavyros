%define fontname	Atavyros
%define name		fonts-otf-%{fontname}
%define version		1.01
%define release		3

%define fontdir		%{_datadir}/fonts/OTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Unicode Atavyros fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://users.teilar.gr/~g1951d/%{fontname}.zip
License:	Public Domain
Group:		System/Fonts/True type
Url:		http://users.teilar.gr/~g1951d/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires: fontconfig
BuildRequires:	mkfontscale, mkfontdir

%description
Robert Granjon (1513 - 1589) produced his Parangonne Greque typeface
(garmond size) at the instigation of Christophe Plantin as a
counterpart to Garamond's Grec du roi, in Antwerp Holland, between
1560 - 1565. It was used in Plantin's multilingual Bible of
1572. Versions of Granjon's type were used for the 1692 edition of
Diogenes Laertius and for the Greek-Dutch edition of the New Testament
in 1698, both published by Henric Wetstenium in Amsterdam. A digital
revival was prepared by Ralph P. Hancock for his Vusillus font in
1999. Latin and Cyrillic are based on a Goudy typeface. The font
covers the Windows Glyph List, Greek Extended, various typographic
extras and some Open Type features (Numerators, Denominators,
Fractions, Old Style Figures, Historical Forms, Stylistic Alternates,
Ligatures).

%prep
%setup -q -c %{name}-%{version}

%install
%__rm -rf %{buildroot}

%__install -m 0755 -d %{buildroot}%{fontdir}
%__install -m 0644 *.otf %{buildroot}%{fontdir}
mkfontscale %{buildroot}%{fontdir}
mkfontdir %{buildroot}%{fontdir}

%__install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/otf-%{fontname}:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{fontconfdir}/otf*
%{fontdir}/*.otf
%{fontdir}/fonts.*



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.01-2mdv2011.0
+ Revision: 675509
- br fontconfig for fc-query used in new rpm-setup-build

* Wed Jul 28 2010 Lev Givon <lev@mandriva.org> 1.01-1mdv2011.0
+ Revision: 562728
- import fonts-otf-Atavyros

