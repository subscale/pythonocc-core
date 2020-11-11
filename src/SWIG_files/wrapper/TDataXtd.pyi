from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TDF import *
from OCC.Core.TDataStd import *
from OCC.Core.gp import *
from OCC.Core.TNaming import *
from OCC.Core.Quantity import *
from OCC.Core.TopoDS import *
from OCC.Core.Poly import *
from OCC.Core.TShort import *


class TDataXtd_Array1OfTrsf:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> gp_Trsf: ...
    def __setitem__(self, index: int, value: gp_Trsf) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[gp_Trsf]: ...
    def next(self) -> gp_Trsf: ...
    __next__ = next
    def Init(self, theValue: gp_Trsf) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> gp_Trsf: ...
    def Last(self) -> gp_Trsf: ...
    def Value(self, theIndex: int) -> gp_Trsf: ...
    def SetValue(self, theIndex: int, theValue: gp_Trsf) -> None: ...

class TDataXtd_ConstraintEnum(IntEnum):
	TDataXtd_RADIUS: int = ...
	TDataXtd_DIAMETER: int = ...
	TDataXtd_MINOR_RADIUS: int = ...
	TDataXtd_MAJOR_RADIUS: int = ...
	TDataXtd_TANGENT: int = ...
	TDataXtd_PARALLEL: int = ...
	TDataXtd_PERPENDICULAR: int = ...
	TDataXtd_CONCENTRIC: int = ...
	TDataXtd_COINCIDENT: int = ...
	TDataXtd_DISTANCE: int = ...
	TDataXtd_ANGLE: int = ...
	TDataXtd_EQUAL_RADIUS: int = ...
	TDataXtd_SYMMETRY: int = ...
	TDataXtd_MIDPOINT: int = ...
	TDataXtd_EQUAL_DISTANCE: int = ...
	TDataXtd_FIX: int = ...
	TDataXtd_RIGID: int = ...
	TDataXtd_FROM: int = ...
	TDataXtd_AXIS: int = ...
	TDataXtd_MATE: int = ...
	TDataXtd_ALIGN_FACES: int = ...
	TDataXtd_ALIGN_AXES: int = ...
	TDataXtd_AXES_ANGLE: int = ...
	TDataXtd_FACES_ANGLE: int = ...
	TDataXtd_ROUND: int = ...
	TDataXtd_OFFSET: int = ...
TDataXtd_RADIUS = TDataXtd_ConstraintEnum.TDataXtd_RADIUS
TDataXtd_DIAMETER = TDataXtd_ConstraintEnum.TDataXtd_DIAMETER
TDataXtd_MINOR_RADIUS = TDataXtd_ConstraintEnum.TDataXtd_MINOR_RADIUS
TDataXtd_MAJOR_RADIUS = TDataXtd_ConstraintEnum.TDataXtd_MAJOR_RADIUS
TDataXtd_TANGENT = TDataXtd_ConstraintEnum.TDataXtd_TANGENT
TDataXtd_PARALLEL = TDataXtd_ConstraintEnum.TDataXtd_PARALLEL
TDataXtd_PERPENDICULAR = TDataXtd_ConstraintEnum.TDataXtd_PERPENDICULAR
TDataXtd_CONCENTRIC = TDataXtd_ConstraintEnum.TDataXtd_CONCENTRIC
TDataXtd_COINCIDENT = TDataXtd_ConstraintEnum.TDataXtd_COINCIDENT
TDataXtd_DISTANCE = TDataXtd_ConstraintEnum.TDataXtd_DISTANCE
TDataXtd_ANGLE = TDataXtd_ConstraintEnum.TDataXtd_ANGLE
TDataXtd_EQUAL_RADIUS = TDataXtd_ConstraintEnum.TDataXtd_EQUAL_RADIUS
TDataXtd_SYMMETRY = TDataXtd_ConstraintEnum.TDataXtd_SYMMETRY
TDataXtd_MIDPOINT = TDataXtd_ConstraintEnum.TDataXtd_MIDPOINT
TDataXtd_EQUAL_DISTANCE = TDataXtd_ConstraintEnum.TDataXtd_EQUAL_DISTANCE
TDataXtd_FIX = TDataXtd_ConstraintEnum.TDataXtd_FIX
TDataXtd_RIGID = TDataXtd_ConstraintEnum.TDataXtd_RIGID
TDataXtd_FROM = TDataXtd_ConstraintEnum.TDataXtd_FROM
TDataXtd_AXIS = TDataXtd_ConstraintEnum.TDataXtd_AXIS
TDataXtd_MATE = TDataXtd_ConstraintEnum.TDataXtd_MATE
TDataXtd_ALIGN_FACES = TDataXtd_ConstraintEnum.TDataXtd_ALIGN_FACES
TDataXtd_ALIGN_AXES = TDataXtd_ConstraintEnum.TDataXtd_ALIGN_AXES
TDataXtd_AXES_ANGLE = TDataXtd_ConstraintEnum.TDataXtd_AXES_ANGLE
TDataXtd_FACES_ANGLE = TDataXtd_ConstraintEnum.TDataXtd_FACES_ANGLE
TDataXtd_ROUND = TDataXtd_ConstraintEnum.TDataXtd_ROUND
TDataXtd_OFFSET = TDataXtd_ConstraintEnum.TDataXtd_OFFSET

class TDataXtd_GeometryEnum(IntEnum):
	TDataXtd_ANY_GEOM: int = ...
	TDataXtd_POINT: int = ...
	TDataXtd_LINE: int = ...
	TDataXtd_CIRCLE: int = ...
	TDataXtd_ELLIPSE: int = ...
	TDataXtd_SPLINE: int = ...
	TDataXtd_PLANE: int = ...
	TDataXtd_CYLINDER: int = ...
TDataXtd_ANY_GEOM = TDataXtd_GeometryEnum.TDataXtd_ANY_GEOM
TDataXtd_POINT = TDataXtd_GeometryEnum.TDataXtd_POINT
TDataXtd_LINE = TDataXtd_GeometryEnum.TDataXtd_LINE
TDataXtd_CIRCLE = TDataXtd_GeometryEnum.TDataXtd_CIRCLE
TDataXtd_ELLIPSE = TDataXtd_GeometryEnum.TDataXtd_ELLIPSE
TDataXtd_SPLINE = TDataXtd_GeometryEnum.TDataXtd_SPLINE
TDataXtd_PLANE = TDataXtd_GeometryEnum.TDataXtd_PLANE
TDataXtd_CYLINDER = TDataXtd_GeometryEnum.TDataXtd_CYLINDER

class tdataxtd:
	@staticmethod
	def IDList(anIDList: TDF_IDList) -> None: ...

class TDataXtd_Axis(TDataStd_GenericEmpty):
	def __init__(self) -> None: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	@overload
	@staticmethod
	def Set(label: TDF_Label) -> TDataXtd_Axis: ...
	@overload
	@staticmethod
	def Set(label: TDF_Label, L: gp_Lin) -> TDataXtd_Axis: ...

class TDataXtd_Constraint(TDF_Attribute):
	def __init__(self) -> None: ...
	def ClearGeometries(self) -> None: ...
	@staticmethod
	def CollectChildConstraints(aLabel: TDF_Label, TheList: TDF_LabelList) -> None: ...
	def GetGeometry(self, Index: int) -> TNaming_NamedShape: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def GetPlane(self) -> TNaming_NamedShape: ...
	def GetType(self) -> TDataXtd_ConstraintEnum: ...
	def GetValue(self) -> TDataStd_Real: ...
	def ID(self) -> Standard_GUID: ...
	@overload
	def Inverted(self, status: bool) -> None: ...
	@overload
	def Inverted(self) -> bool: ...
	def IsDimension(self) -> bool: ...
	def IsPlanar(self) -> bool: ...
	def NbGeometries(self) -> int: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def References(self, DS: TDF_DataSet) -> None: ...
	def Restore(self, With: TDF_Attribute) -> None: ...
	@overload
	def Reversed(self, status: bool) -> None: ...
	@overload
	def Reversed(self) -> bool: ...
	@overload
	@staticmethod
	def Set(label: TDF_Label) -> TDataXtd_Constraint: ...
	@overload
	def Set(self, type: TDataXtd_ConstraintEnum, G1: TNaming_NamedShape) -> None: ...
	@overload
	def Set(self, type: TDataXtd_ConstraintEnum, G1: TNaming_NamedShape, G2: TNaming_NamedShape) -> None: ...
	@overload
	def Set(self, type: TDataXtd_ConstraintEnum, G1: TNaming_NamedShape, G2: TNaming_NamedShape, G3: TNaming_NamedShape) -> None: ...
	@overload
	def Set(self, type: TDataXtd_ConstraintEnum, G1: TNaming_NamedShape, G2: TNaming_NamedShape, G3: TNaming_NamedShape, G4: TNaming_NamedShape) -> None: ...
	def SetGeometry(self, Index: int, G: TNaming_NamedShape) -> None: ...
	def SetPlane(self, plane: TNaming_NamedShape) -> None: ...
	def SetType(self, CTR: TDataXtd_ConstraintEnum) -> None: ...
	def SetValue(self, V: TDataStd_Real) -> None: ...
	@overload
	def Verified(self) -> bool: ...
	@overload
	def Verified(self, status: bool) -> None: ...

class TDataXtd_Geometry(TDF_Attribute):
	def __init__(self) -> None: ...
	@overload
	@staticmethod
	def Axis(L: TDF_Label, G: gp_Ax1) -> bool: ...
	@overload
	@staticmethod
	def Axis(S: TNaming_NamedShape, G: gp_Ax1) -> bool: ...
	@overload
	@staticmethod
	def Circle(L: TDF_Label, G: gp_Circ) -> bool: ...
	@overload
	@staticmethod
	def Circle(S: TNaming_NamedShape, G: gp_Circ) -> bool: ...
	@overload
	@staticmethod
	def Cylinder(L: TDF_Label, G: gp_Cylinder) -> bool: ...
	@overload
	@staticmethod
	def Cylinder(S: TNaming_NamedShape, G: gp_Cylinder) -> bool: ...
	@overload
	@staticmethod
	def Ellipse(L: TDF_Label, G: gp_Elips) -> bool: ...
	@overload
	@staticmethod
	def Ellipse(S: TNaming_NamedShape, G: gp_Elips) -> bool: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def GetType(self) -> TDataXtd_GeometryEnum: ...
	def ID(self) -> Standard_GUID: ...
	@overload
	@staticmethod
	def Line(L: TDF_Label, G: gp_Lin) -> bool: ...
	@overload
	@staticmethod
	def Line(S: TNaming_NamedShape, G: gp_Lin) -> bool: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	@overload
	@staticmethod
	def Plane(L: TDF_Label, G: gp_Pln) -> bool: ...
	@overload
	@staticmethod
	def Plane(S: TNaming_NamedShape, G: gp_Pln) -> bool: ...
	@overload
	@staticmethod
	def Point(L: TDF_Label, G: gp_Pnt) -> bool: ...
	@overload
	@staticmethod
	def Point(S: TNaming_NamedShape, G: gp_Pnt) -> bool: ...
	def Restore(self, with_: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(label: TDF_Label) -> TDataXtd_Geometry: ...
	def SetType(self, T: TDataXtd_GeometryEnum) -> None: ...
	@overload
	@staticmethod
	def Type(L: TDF_Label) -> TDataXtd_GeometryEnum: ...
	@overload
	@staticmethod
	def Type(S: TNaming_NamedShape) -> TDataXtd_GeometryEnum: ...

class TDataXtd_Pattern(TDF_Attribute):
	def ComputeTrsfs(self, Trsfs: TDataXtd_Array1OfTrsf) -> None: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	def NbTrsfs(self) -> int: ...
	def PatternID(self) -> Standard_GUID: ...

class TDataXtd_Placement(TDataStd_GenericEmpty):
	def __init__(self) -> None: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	@staticmethod
	def Set(label: TDF_Label) -> TDataXtd_Placement: ...

class TDataXtd_Plane(TDataStd_GenericEmpty):
	def __init__(self) -> None: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	@overload
	@staticmethod
	def Set(label: TDF_Label) -> TDataXtd_Plane: ...
	@overload
	@staticmethod
	def Set(label: TDF_Label, P: gp_Pln) -> TDataXtd_Plane: ...

class TDataXtd_Point(TDataStd_GenericEmpty):
	def __init__(self) -> None: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	@overload
	@staticmethod
	def Set(label: TDF_Label) -> TDataXtd_Point: ...
	@overload
	@staticmethod
	def Set(label: TDF_Label, P: gp_Pnt) -> TDataXtd_Point: ...

class TDataXtd_Position(TDF_Attribute):
	def __init__(self) -> None: ...
	@staticmethod
	def Get(aLabel: TDF_Label, aPos: gp_Pnt) -> bool: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def GetPosition(self) -> gp_Pnt: ...
	def ID(self) -> Standard_GUID: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, intoAttribute: TDF_Attribute, aRelocTationable: TDF_RelocationTable) -> None: ...
	def Restore(self, anAttribute: TDF_Attribute) -> None: ...
	@overload
	@staticmethod
	def Set(aLabel: TDF_Label, aPos: gp_Pnt) -> None: ...
	@overload
	@staticmethod
	def Set(aLabel: TDF_Label) -> TDataXtd_Position: ...
	def SetPosition(self, aPos: gp_Pnt) -> None: ...

class TDataXtd_Presentation(TDF_Attribute):
	def __init__(self) -> None: ...
	def AddSelectionMode(self, theSelectionMode: int, theTransaction: Optional[bool] = True) -> None: ...
	def BackupCopy(self) -> TDF_Attribute: ...
	def Color(self) -> Quantity_NameOfColor: ...
	def GetDriverGUID(self) -> Standard_GUID: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def GetNbSelectionModes(self) -> int: ...
	def HasOwnColor(self) -> bool: ...
	def HasOwnMaterial(self) -> bool: ...
	def HasOwnMode(self) -> bool: ...
	def HasOwnSelectionMode(self) -> bool: ...
	def HasOwnTransparency(self) -> bool: ...
	def HasOwnWidth(self) -> bool: ...
	def ID(self) -> Standard_GUID: ...
	def IsDisplayed(self) -> bool: ...
	def MaterialIndex(self) -> int: ...
	def Mode(self) -> int: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, intoAttribute: TDF_Attribute, aRelocTationable: TDF_RelocationTable) -> None: ...
	def Restore(self, anAttribute: TDF_Attribute) -> None: ...
	def SelectionMode(self, index: Optional[int] = 1) -> int: ...
	@staticmethod
	def Set(theLabel: TDF_Label, theDriverId: Standard_GUID) -> TDataXtd_Presentation: ...
	def SetColor(self, theColor: Quantity_NameOfColor) -> None: ...
	def SetDisplayed(self, theIsDisplayed: bool) -> None: ...
	def SetDriverGUID(self, theGUID: Standard_GUID) -> None: ...
	def SetMaterialIndex(self, theMaterialIndex: int) -> None: ...
	def SetMode(self, theMode: int) -> None: ...
	def SetSelectionMode(self, theSelectionMode: int, theTransaction: Optional[bool] = True) -> None: ...
	def SetTransparency(self, theValue: float) -> None: ...
	def SetWidth(self, theWidth: float) -> None: ...
	def Transparency(self) -> float: ...
	@staticmethod
	def Unset(theLabel: TDF_Label) -> None: ...
	def UnsetColor(self) -> None: ...
	def UnsetMaterial(self) -> None: ...
	def UnsetMode(self) -> None: ...
	def UnsetSelectionMode(self) -> None: ...
	def UnsetTransparency(self) -> None: ...
	def UnsetWidth(self) -> None: ...
	def Width(self) -> float: ...
	@staticmethod
	def getColorNameFromOldEnum(theOld: int) -> Quantity_NameOfColor: ...
	@staticmethod
	def getOldColorNameFromNewEnum(theNew: Quantity_NameOfColor) -> int: ...

class TDataXtd_Shape(TDataStd_GenericEmpty):
	def __init__(self) -> None: ...
	@staticmethod
	def Find(current: TDF_Label, S: TDataXtd_Shape) -> bool: ...
	@staticmethod
	def Get(label: TDF_Label) -> TopoDS_Shape: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	@staticmethod
	def New(label: TDF_Label) -> TDataXtd_Shape: ...
	def References(self, DS: TDF_DataSet) -> None: ...
	@staticmethod
	def Set(label: TDF_Label, shape: TopoDS_Shape) -> TDataXtd_Shape: ...

class TDataXtd_Triangulation(TDF_Attribute):
	def __init__(self) -> None: ...
	@overload
	def Deflection(self) -> float: ...
	@overload
	def Deflection(self, theDeflection: float) -> None: ...
	def Get(self) -> Poly_Triangulation: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def HasNormals(self) -> bool: ...
	def HasUVNodes(self) -> bool: ...
	def ID(self) -> Standard_GUID: ...
	def NbNodes(self) -> int: ...
	def NbTriangles(self) -> int: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Node(self, theIndex: int) -> gp_Pnt: ...
	def Normal(self, theIndex: int) -> gp_Dir: ...
	def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def RemoveUVNodes(self) -> None: ...
	def Restore(self, theAttribute: TDF_Attribute) -> None: ...
	@overload
	@staticmethod
	def Set(theLabel: TDF_Label) -> TDataXtd_Triangulation: ...
	@overload
	@staticmethod
	def Set(theLabel: TDF_Label, theTriangulation: Poly_Triangulation) -> TDataXtd_Triangulation: ...
	@overload
	def Set(self, theTriangulation: Poly_Triangulation) -> None: ...
	def SetNode(self, theIndex: int, theNode: gp_Pnt) -> None: ...
	def SetNormal(self, theIndex: int, theNormal: gp_Dir) -> None: ...
	def SetNormals(self, theNormals: TShort_HArray1OfShortReal) -> None: ...
	def SetTriangle(self, theIndex: int, theTriangle: Poly_Triangle) -> None: ...
	def SetUVNode(self, theIndex: int, theUVNode: gp_Pnt2d) -> None: ...
	def Triangle(self, theIndex: int) -> Poly_Triangle: ...
	def UVNode(self, theIndex: int) -> gp_Pnt2d: ...

class TDataXtd_PatternStd(TDataXtd_Pattern):
	def __init__(self) -> None: ...
	@overload
	def Axis1(self, Axis1: TNaming_NamedShape) -> None: ...
	@overload
	def Axis1(self) -> TNaming_NamedShape: ...
	@overload
	def Axis1Reversed(self, Axis1Reversed: bool) -> None: ...
	@overload
	def Axis1Reversed(self) -> bool: ...
	@overload
	def Axis2(self, Axis2: TNaming_NamedShape) -> None: ...
	@overload
	def Axis2(self) -> TNaming_NamedShape: ...
	@overload
	def Axis2Reversed(self, Axis2Reversed: bool) -> None: ...
	@overload
	def Axis2Reversed(self) -> bool: ...
	def ComputeTrsfs(self, Trsfs: TDataXtd_Array1OfTrsf) -> None: ...
	@staticmethod
	def GetPatternID() -> Standard_GUID: ...
	@overload
	def Mirror(self, plane: TNaming_NamedShape) -> None: ...
	@overload
	def Mirror(self) -> TNaming_NamedShape: ...
	@overload
	def NbInstances1(self, NbInstances1: TDataStd_Integer) -> None: ...
	@overload
	def NbInstances1(self) -> TDataStd_Integer: ...
	@overload
	def NbInstances2(self, NbInstances2: TDataStd_Integer) -> None: ...
	@overload
	def NbInstances2(self) -> TDataStd_Integer: ...
	def NbTrsfs(self) -> int: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def PatternID(self) -> Standard_GUID: ...
	def References(self, aDataSet: TDF_DataSet) -> None: ...
	def Restore(self, With: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(label: TDF_Label) -> TDataXtd_PatternStd: ...
	@overload
	def Signature(self, signature: int) -> None: ...
	@overload
	def Signature(self) -> int: ...
	@overload
	def Value1(self, value: TDataStd_Real) -> None: ...
	@overload
	def Value1(self) -> TDataStd_Real: ...
	@overload
	def Value2(self, value: TDataStd_Real) -> None: ...
	@overload
	def Value2(self) -> TDataStd_Real: ...

# harray1 classes

class TDataXtd_HArray1OfTrsf(TDataXtd_Array1OfTrsf, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> TDataXtd_Array1OfTrsf: ...

# harray2 classes
# hsequence classes

tdataxtd_IDList = tdataxtd.IDList
tdataxtd_Print = tdataxtd.Print
tdataxtd_Print = tdataxtd.Print
TDataXtd_Axis_GetID = TDataXtd_Axis.GetID
TDataXtd_Axis_Set = TDataXtd_Axis.Set
TDataXtd_Axis_Set = TDataXtd_Axis.Set
TDataXtd_Constraint_CollectChildConstraints = TDataXtd_Constraint.CollectChildConstraints
TDataXtd_Constraint_GetID = TDataXtd_Constraint.GetID
TDataXtd_Constraint_Set = TDataXtd_Constraint.Set
TDataXtd_Geometry_Axis = TDataXtd_Geometry.Axis
TDataXtd_Geometry_Axis = TDataXtd_Geometry.Axis
TDataXtd_Geometry_Circle = TDataXtd_Geometry.Circle
TDataXtd_Geometry_Circle = TDataXtd_Geometry.Circle
TDataXtd_Geometry_Cylinder = TDataXtd_Geometry.Cylinder
TDataXtd_Geometry_Cylinder = TDataXtd_Geometry.Cylinder
TDataXtd_Geometry_Ellipse = TDataXtd_Geometry.Ellipse
TDataXtd_Geometry_Ellipse = TDataXtd_Geometry.Ellipse
TDataXtd_Geometry_GetID = TDataXtd_Geometry.GetID
TDataXtd_Geometry_Line = TDataXtd_Geometry.Line
TDataXtd_Geometry_Line = TDataXtd_Geometry.Line
TDataXtd_Geometry_Plane = TDataXtd_Geometry.Plane
TDataXtd_Geometry_Plane = TDataXtd_Geometry.Plane
TDataXtd_Geometry_Point = TDataXtd_Geometry.Point
TDataXtd_Geometry_Point = TDataXtd_Geometry.Point
TDataXtd_Geometry_Set = TDataXtd_Geometry.Set
TDataXtd_Geometry_Type = TDataXtd_Geometry.Type
TDataXtd_Geometry_Type = TDataXtd_Geometry.Type
TDataXtd_Pattern_GetID = TDataXtd_Pattern.GetID
TDataXtd_Placement_GetID = TDataXtd_Placement.GetID
TDataXtd_Placement_Set = TDataXtd_Placement.Set
TDataXtd_Plane_GetID = TDataXtd_Plane.GetID
TDataXtd_Plane_Set = TDataXtd_Plane.Set
TDataXtd_Plane_Set = TDataXtd_Plane.Set
TDataXtd_Point_GetID = TDataXtd_Point.GetID
TDataXtd_Point_Set = TDataXtd_Point.Set
TDataXtd_Point_Set = TDataXtd_Point.Set
TDataXtd_Position_Get = TDataXtd_Position.Get
TDataXtd_Position_GetID = TDataXtd_Position.GetID
TDataXtd_Position_Set = TDataXtd_Position.Set
TDataXtd_Position_Set = TDataXtd_Position.Set
TDataXtd_Presentation_GetID = TDataXtd_Presentation.GetID
TDataXtd_Presentation_Set = TDataXtd_Presentation.Set
TDataXtd_Presentation_Unset = TDataXtd_Presentation.Unset
TDataXtd_Presentation_getColorNameFromOldEnum = TDataXtd_Presentation.getColorNameFromOldEnum
TDataXtd_Presentation_getOldColorNameFromNewEnum = TDataXtd_Presentation.getOldColorNameFromNewEnum
TDataXtd_Shape_Find = TDataXtd_Shape.Find
TDataXtd_Shape_Get = TDataXtd_Shape.Get
TDataXtd_Shape_GetID = TDataXtd_Shape.GetID
TDataXtd_Shape_New = TDataXtd_Shape.New
TDataXtd_Shape_Set = TDataXtd_Shape.Set
TDataXtd_Triangulation_GetID = TDataXtd_Triangulation.GetID
TDataXtd_Triangulation_Set = TDataXtd_Triangulation.Set
TDataXtd_Triangulation_Set = TDataXtd_Triangulation.Set
TDataXtd_PatternStd_GetPatternID = TDataXtd_PatternStd.GetPatternID
TDataXtd_PatternStd_Set = TDataXtd_PatternStd.Set
