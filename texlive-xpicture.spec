# revision 28770
# category Package
# catalog-ctan /macros/latex/contrib/xpicture
# catalog-date 2013-01-08 10:49:23 +0100
# catalog-license lppl1.3
# catalog-version 1.2a
Name:		texlive-xpicture
Version:	1.2a
Release:	10
Summary:	Extensions of LaTeX picture drawing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xpicture
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpicture.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpicture.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpicture.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends the facilities of the pict2e and the
curve2e packages, providing extra reference frames, conic
section curves, graphs of elementary functions and other
parametric curves.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xpicture/xpicture.sty
%doc %{_texmfdistdir}/doc/latex/xpicture/README
%doc %{_texmfdistdir}/doc/latex/xpicture/xpicture-doc.pdf
%doc %{_texmfdistdir}/doc/latex/xpicture/xpicture-doc.tex
%doc %{_texmfdistdir}/doc/latex/xpicture/xpicture.cfgxmpl
%doc %{_texmfdistdir}/doc/latex/xpicture/xpicture.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xpicture/xpicture.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
