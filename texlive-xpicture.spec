Name:		texlive-xpicture
Version:	28770
Release:	1
Summary:	Extensions of LaTeX picture drawing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xpicture
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpicture.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpicture.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpicture.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
