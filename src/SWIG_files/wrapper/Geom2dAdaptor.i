/*
Copyright 2008-2022 Thomas Paviot (tpaviot@gmail.com)

This file is part of pythonOCC.
pythonOCC is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pythonOCC is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.
*/
%define GEOM2DADAPTORDOCSTRING
"Geom2dAdaptor module, see official documentation at
https://www.opencascade.com/doc/occt-7.6.0/refman/html/package_geom2dadaptor.html"
%enddef
%module (package="OCC.Core", docstring=GEOM2DADAPTORDOCSTRING) Geom2dAdaptor


%{
#ifdef WNT
#pragma warning(disable : 4716)
#endif
%}

%include ../common/CommonIncludes.i
%include ../common/ExceptionCatcher.i
%include ../common/FunctionTransformers.i
%include ../common/EnumTemplates.i
%include ../common/Operators.i
%include ../common/OccHandle.i


%{
#include<Geom2dAdaptor_module.hxx>

//Dependencies
#include<Standard_module.hxx>
#include<NCollection_module.hxx>
#include<Adaptor2d_module.hxx>
#include<Geom2d_module.hxx>
#include<gp_module.hxx>
#include<GeomAbs_module.hxx>
#include<TColStd_module.hxx>
#include<TColgp_module.hxx>
#include<TColStd_module.hxx>
#include<TCollection_module.hxx>
#include<Storage_module.hxx>
%};
%import Standard.i
%import NCollection.i
%import Adaptor2d.i
%import Geom2d.i
%import gp.i
%import GeomAbs.i
%import TColStd.i

%pythoncode {
from enum import IntEnum
from OCC.Core.Exception import *
};

/* public enums */
/* end public enums declaration */

/* python proxy classes for enums */
%pythoncode {
};
/* end python proxy for enums */

/* handles */
%wrap_handle(Geom2dAdaptor_Curve)
/* end handles declaration */

/* templates */
/* end templates declaration */

/* typedefs */
/* end typedefs declaration */

/**********************
* class Geom2dAdaptor *
**********************/
%rename(geom2dadaptor) Geom2dAdaptor;
class Geom2dAdaptor {
	public:
		/****************** MakeCurve ******************/
		/**** md5 signature: c72e8d90e9cff395d1b9d0b5bc484109 ****/
		%feature("compactdefaultargs") MakeCurve;
		%feature("autodoc", "Inherited from ghcurve. provides a curve handled by reference. creates a 2d curve from a hcurve2d. this cannot process the othercurves.

Parameters
----------
HC: Adaptor2d_Curve2d

Returns
-------
opencascade::handle<Geom2d_Curve>
") MakeCurve;
		static opencascade::handle<Geom2d_Curve> MakeCurve(const Adaptor2d_Curve2d & HC);

};


%extend Geom2dAdaptor {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/****************************
* class Geom2dAdaptor_Curve *
****************************/
class Geom2dAdaptor_Curve : public Adaptor2d_Curve2d {
	public:
		/****************** Geom2dAdaptor_Curve ******************/
		/**** md5 signature: 2791dbc26639b96186559159a2815b29 ****/
		%feature("compactdefaultargs") Geom2dAdaptor_Curve;
		%feature("autodoc", "No available documentation.

Returns
-------
None
") Geom2dAdaptor_Curve;
		 Geom2dAdaptor_Curve();

		/****************** Geom2dAdaptor_Curve ******************/
		/**** md5 signature: e0e393202c576f2801d7e2429a622a66 ****/
		%feature("compactdefaultargs") Geom2dAdaptor_Curve;
		%feature("autodoc", "No available documentation.

Parameters
----------
C: Geom2d_Curve

Returns
-------
None
") Geom2dAdaptor_Curve;
		 Geom2dAdaptor_Curve(const opencascade::handle<Geom2d_Curve> & C);

		/****************** Geom2dAdaptor_Curve ******************/
		/**** md5 signature: 68f15594f006f79ed7f5d7313c319ebe ****/
		%feature("compactdefaultargs") Geom2dAdaptor_Curve;
		%feature("autodoc", "Standard_constructionerror is raised if ufirst>ulast.

Parameters
----------
C: Geom2d_Curve
UFirst: float
ULast: float

Returns
-------
None
") Geom2dAdaptor_Curve;
		 Geom2dAdaptor_Curve(const opencascade::handle<Geom2d_Curve> & C, const Standard_Real UFirst, const Standard_Real ULast);

		/****************** BSpline ******************/
		/**** md5 signature: 9439c331c4f14f299277aa5a4ff16cec ****/
		%feature("compactdefaultargs") BSpline;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<Geom2d_BSplineCurve>
") BSpline;
		opencascade::handle<Geom2d_BSplineCurve> BSpline();

		/****************** Bezier ******************/
		/**** md5 signature: cabcbe9e94c679dcfc142972b20ab60b ****/
		%feature("compactdefaultargs") Bezier;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<Geom2d_BezierCurve>
") Bezier;
		opencascade::handle<Geom2d_BezierCurve> Bezier();

		/****************** Circle ******************/
		/**** md5 signature: 031880777795958cc554fa5739cb3a95 ****/
		%feature("compactdefaultargs") Circle;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Circ2d
") Circle;
		gp_Circ2d Circle();

		/****************** Continuity ******************/
		/**** md5 signature: 9381b370dfdd50af7f1b79ce202f0c6f ****/
		%feature("compactdefaultargs") Continuity;
		%feature("autodoc", "No available documentation.

Returns
-------
GeomAbs_Shape
") Continuity;
		GeomAbs_Shape Continuity();

		/****************** Curve ******************/
		/**** md5 signature: e09aeee135451614c1573555e3da507c ****/
		%feature("compactdefaultargs") Curve;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<Geom2d_Curve>
") Curve;
		const opencascade::handle<Geom2d_Curve> & Curve();

		/****************** D0 ******************/
		/**** md5 signature: 01a5234aae6db090351bac35b3718fd9 ****/
		%feature("compactdefaultargs") D0;
		%feature("autodoc", "Computes the point of parameter u.

Parameters
----------
U: float
P: gp_Pnt2d

Returns
-------
None
") D0;
		void D0(const Standard_Real U, gp_Pnt2d & P);

		/****************** D1 ******************/
		/**** md5 signature: 79a293d0b91ab6d1359881075119fb56 ****/
		%feature("compactdefaultargs") D1;
		%feature("autodoc", "Computes the point of parameter u on the curve with its first derivative. raised if the continuity of the current interval is not c1.

Parameters
----------
U: float
P: gp_Pnt2d
V: gp_Vec2d

Returns
-------
None
") D1;
		void D1(const Standard_Real U, gp_Pnt2d & P, gp_Vec2d & V);

		/****************** D2 ******************/
		/**** md5 signature: acc8c0955596bb0bf809102736ad1124 ****/
		%feature("compactdefaultargs") D2;
		%feature("autodoc", "Returns the point p of parameter u, the first and second derivatives v1 and v2. raised if the continuity of the current interval is not c2.

Parameters
----------
U: float
P: gp_Pnt2d
V1: gp_Vec2d
V2: gp_Vec2d

Returns
-------
None
") D2;
		void D2(const Standard_Real U, gp_Pnt2d & P, gp_Vec2d & V1, gp_Vec2d & V2);

		/****************** D3 ******************/
		/**** md5 signature: 28315b7efe2f6c64fe9497aa5c5ddaf6 ****/
		%feature("compactdefaultargs") D3;
		%feature("autodoc", "Returns the point p of parameter u, the first, the second and the third derivative. raised if the continuity of the current interval is not c3.

Parameters
----------
U: float
P: gp_Pnt2d
V1: gp_Vec2d
V2: gp_Vec2d
V3: gp_Vec2d

Returns
-------
None
") D3;
		void D3(const Standard_Real U, gp_Pnt2d & P, gp_Vec2d & V1, gp_Vec2d & V2, gp_Vec2d & V3);

		/****************** DN ******************/
		/**** md5 signature: a05d2f76912764cef5ac7bb40ebda3d7 ****/
		%feature("compactdefaultargs") DN;
		%feature("autodoc", "The returned vector gives the value of the derivative for the order of derivation n. raised if the continuity of the current interval is not cn. raised if n < 1.

Parameters
----------
U: float
N: int

Returns
-------
gp_Vec2d
") DN;
		gp_Vec2d DN(const Standard_Real U, const Standard_Integer N);

		/****************** Degree ******************/
		/**** md5 signature: 5ce473e72cc7bb935a667f4c839dab09 ****/
		%feature("compactdefaultargs") Degree;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") Degree;
		Standard_Integer Degree();

		/****************** Ellipse ******************/
		/**** md5 signature: 57e9088d9546fb79032102b676477b62 ****/
		%feature("compactdefaultargs") Ellipse;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Elips2d
") Ellipse;
		gp_Elips2d Ellipse();

		/****************** FirstParameter ******************/
		/**** md5 signature: 93c381754667baab23468a195644e410 ****/
		%feature("compactdefaultargs") FirstParameter;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") FirstParameter;
		virtual Standard_Real FirstParameter();

		/****************** GetType ******************/
		/**** md5 signature: eaef05bb051ab4b74eda73aca8930d16 ****/
		%feature("compactdefaultargs") GetType;
		%feature("autodoc", "No available documentation.

Returns
-------
GeomAbs_CurveType
") GetType;
		virtual GeomAbs_CurveType GetType();

		/****************** Hyperbola ******************/
		/**** md5 signature: 951e1971b5974627f011740e5c4c9ecb ****/
		%feature("compactdefaultargs") Hyperbola;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Hypr2d
") Hyperbola;
		gp_Hypr2d Hyperbola();

		/****************** Intervals ******************/
		/**** md5 signature: fc573cb56cf1a9c05ee189fd913ff6f5 ****/
		%feature("compactdefaultargs") Intervals;
		%feature("autodoc", "Stores in <t> the parameters bounding the intervals of continuity <s>. //! the array must provide enough room to accommodate for the parameters. i.e. t.length() > nbintervals().

Parameters
----------
T: TColStd_Array1OfReal
S: GeomAbs_Shape

Returns
-------
None
") Intervals;
		void Intervals(TColStd_Array1OfReal & T, const GeomAbs_Shape S);

		/****************** IsClosed ******************/
		/**** md5 signature: 00978070ec4cb5f00d1d002a8d5d3763 ****/
		%feature("compactdefaultargs") IsClosed;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsClosed;
		Standard_Boolean IsClosed();

		/****************** IsPeriodic ******************/
		/**** md5 signature: 15e3ccfd3ad4ae42959489f7f64aa8ca ****/
		%feature("compactdefaultargs") IsPeriodic;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsPeriodic;
		Standard_Boolean IsPeriodic();

		/****************** IsRational ******************/
		/**** md5 signature: 82ca56fad113156125f40128b25c0d8e ****/
		%feature("compactdefaultargs") IsRational;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsRational;
		Standard_Boolean IsRational();

		/****************** LastParameter ******************/
		/**** md5 signature: a2893a92f9c4af09acb0cd59d959d964 ****/
		%feature("compactdefaultargs") LastParameter;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") LastParameter;
		virtual Standard_Real LastParameter();

		/****************** Line ******************/
		/**** md5 signature: d41344e9c3febf8a7347a9e78e837373 ****/
		%feature("compactdefaultargs") Line;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Lin2d
") Line;
		gp_Lin2d Line();

		/****************** Load ******************/
		/**** md5 signature: 2541208b3ec77b0ab58dcd00b56be7d9 ****/
		%feature("compactdefaultargs") Load;
		%feature("autodoc", "No available documentation.

Parameters
----------
theCurve: Geom2d_Curve

Returns
-------
None
") Load;
		void Load(const opencascade::handle<Geom2d_Curve> & theCurve);

		/****************** Load ******************/
		/**** md5 signature: 7a0e04bf8c70800ef741c293e6f1853c ****/
		%feature("compactdefaultargs") Load;
		%feature("autodoc", "Standard_constructionerror is raised if theufirst>theulast.

Parameters
----------
theCurve: Geom2d_Curve
theUFirst: float
theULast: float

Returns
-------
None
") Load;
		void Load(const opencascade::handle<Geom2d_Curve> & theCurve, const Standard_Real theUFirst, const Standard_Real theULast);

		/****************** NbIntervals ******************/
		/**** md5 signature: 8ce4f61bff96d1ce0784028b47edd8dc ****/
		%feature("compactdefaultargs") NbIntervals;
		%feature("autodoc", "If necessary, breaks the curve in intervals of continuity <s>. and returns the number of intervals.

Parameters
----------
S: GeomAbs_Shape

Returns
-------
int
") NbIntervals;
		Standard_Integer NbIntervals(const GeomAbs_Shape S);

		/****************** NbKnots ******************/
		/**** md5 signature: 841663cbf96bec3b939f307c52df6c7c ****/
		%feature("compactdefaultargs") NbKnots;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbKnots;
		Standard_Integer NbKnots();

		/****************** NbPoles ******************/
		/**** md5 signature: 52e5fadf897540545847ef59cc0ba942 ****/
		%feature("compactdefaultargs") NbPoles;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbPoles;
		Standard_Integer NbPoles();

		/****************** NbSamples ******************/
		/**** md5 signature: b50a2e2af8c6f92fd1d1eba428d764af ****/
		%feature("compactdefaultargs") NbSamples;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbSamples;
		virtual Standard_Integer NbSamples();

		/****************** Parabola ******************/
		/**** md5 signature: 38729705f952495154cecf7cf9964648 ****/
		%feature("compactdefaultargs") Parabola;
		%feature("autodoc", "No available documentation.

Returns
-------
gp_Parab2d
") Parabola;
		gp_Parab2d Parabola();

		/****************** Period ******************/
		/**** md5 signature: 88909a321398632744c0d6841580c626 ****/
		%feature("compactdefaultargs") Period;
		%feature("autodoc", "No available documentation.

Returns
-------
float
") Period;
		Standard_Real Period();

		/****************** Reset ******************/
		/**** md5 signature: 7beb446fe26b948f797f8de87e46c23d ****/
		%feature("compactdefaultargs") Reset;
		%feature("autodoc", "Reset currently loaded curve (undone load()).

Returns
-------
None
") Reset;
		void Reset();

		/****************** Resolution ******************/
		/**** md5 signature: 1c5e768832095b165fef245795734120 ****/
		%feature("compactdefaultargs") Resolution;
		%feature("autodoc", "Returns the parametric resolution.

Parameters
----------
Ruv: float

Returns
-------
float
") Resolution;
		Standard_Real Resolution(const Standard_Real Ruv);

		/****************** Trim ******************/
		/**** md5 signature: b5ce1c7f3b02aa6680da8e9ad704acc6 ****/
		%feature("compactdefaultargs") Trim;
		%feature("autodoc", "Returns a curve equivalent of <self> between parameters <first> and <last>. <tol> is used to test for 3d points confusion. if <first> >= <last>.

Parameters
----------
First: float
Last: float
Tol: float

Returns
-------
opencascade::handle<Adaptor2d_Curve2d>
") Trim;
		opencascade::handle<Adaptor2d_Curve2d> Trim(const Standard_Real First, const Standard_Real Last, const Standard_Real Tol);

		/****************** Value ******************/
		/**** md5 signature: 91dcf5c5229f25c64d3a714347090b29 ****/
		%feature("compactdefaultargs") Value;
		%feature("autodoc", "Computes the point of parameter u on the curve.

Parameters
----------
U: float

Returns
-------
gp_Pnt2d
") Value;
		gp_Pnt2d Value(const Standard_Real U);

};


%make_alias(Geom2dAdaptor_Curve)

%extend Geom2dAdaptor_Curve {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/* harray1 classes */
/* harray2 classes */
/* hsequence classes */
/* class aliases */
%pythoncode {
}
/* deprecated methods */
%pythoncode {
@deprecated
def geom2dadaptor_MakeCurve(*args):
	return geom2dadaptor.MakeCurve(*args)

}
