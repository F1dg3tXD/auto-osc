bl_info = {
    "name": "Auto OSC",
    "author": "F1dg3t",
    "version": (1, 0),
    "blender": (3, 3, 0),
    "location": "View3D",
    "description": "Automatically find correct configuration for Add Routes OSC settings",
    "category": "Tool"
}

if "bpy" in locals():
    import importlib
    if "osc_config" in locals():
        importlib.reload(osc_config)

import bpy
from . import osc_config

classes = (osc_config.OSCConfigPanel, osc_config.OBJECT_OT_GetOSCOperator)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
