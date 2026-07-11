%global tl_name xpicture
%global tl_revision 28770

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2a
Release:	%{tl_revision}.1
Summary:	Extensions of LaTeX picture drawing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xpicture
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpicture.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpicture.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpicture.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package extends the facilities of the pict2e and the curve2e
packages, providing extra reference frames, conic section curves, graphs
of elementary functions and other parametric curves.

