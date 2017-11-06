#pragma once

class PropertyFog;
class DepthOfField;
class PropertyGesture;
class PropertyListener;
class ComponentBase;
class PropertyEGuiTexture;
class PropertyBlur;
class VRDeviceComponent;
class PropertyFbxNodeBaseFbxFile;
class EActor;
class Range;
class BoundingBox2D;
class Color;
class EGuiProgressBarPropertyUI;
class PropertyDepthOfField;
class PropertyCube;
class EGuiButton;
class PropertySound;
class CodeFarmComponent;
class Polygon;
class Vector4;
class PropertyKinectSkeleton;
class Line;
class PropertyOcean;
class ScriptComponent;
class Blur;
class PropertyLight;
class AntiAliasing;
class EGuiButtonPropertyUI;
class PropertyCamera;
class PropertyKinectAvatar;
class PropertyInstance;
class Plane;
class Fbx;
class Frustum;
class Sphere;
class EGuiSlider;
class PropertySphere;
class PropertyCylinder;
class KinectAvatarComponent;
class Collision;
class Vector2;
class Util;
class FDMComponent;
class Cube;
class FbxNodeRoot;
class Cylinder;
class Container;
class PropertyScript;
class BoundingBox;
class PropertyEGuiSlider;
class ContainerComponent;
class Point;
class World;
class Matrix;
class Quaternion;
class PropertyMaterial;
class EGuiTexture;
class PropertyNeuron;
class TransformGroup;
class PropertyEGuiLabel;
class RigidMesh;
class Rect;
class GestureComponent;
class NeuronComponent;
class PropertyAntiAliasing;
class Light;
class PlaneMesh;
class EGuiWidget;
class PropertyRigidMesh;
class PropertyShadowMap;
class Bloom;
class FbxNodeBase;
class PropertyTransform;
class PropertyColorFilter;
class PropertyMotionDevice;
class ColorFilter;
class MotionDeviceComponent;
class PropertyFbxNodeMesh;
class Listener;
class Animation;
class FbxNodeMesh;
class PropertyEGuiWidget;
class PropertyBloom;
class KinectImageComponent;
class PropertyGBD;
class Matrix3;
class Vector3;
class PropertyVRDevice;
class PropertyPlaneMesh;
class FbxNodeBone;
class PropertyKinectImage;
class PropertyFbxFile;
class PropertyFbxAnimation;
class EGuiLabel;
class KinectSkeletonComponent;
class EGuiProgressBar;
class Ocean;
class PropertyAnimation;
class Camera;
class Sound;



class sample : public EActor
{
public:
    virtual int OnMessage(wstring msg, int arg0, Vector4* arg1, Vector4* arg2);
public:
    virtual int Update();
public:
    sample();
public:
    virtual const char* __GetClassName__();
    virtual unsigned int __GetFieldNum__();
    virtual const char* __GetFieldName__(unsigned int i);
    virtual const char* __GetFieldType__(unsigned int i);
    virtual const char* __GetFieldAccessor__(unsigned int i);

    virtual int __ReadField__(string fieldName, void* ptr, int* len);
    virtual int __WriteField__(string fieldName, void* ptr, int len, int typeInfo);

private:
    static const	vector<string>	mFieldNames;
    static const	vector<string>	mFieldTypes;
    static const	vector<string>	mFieldAccessors;
};
