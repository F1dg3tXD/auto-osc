import bpy
import socket

def get_best_ports():
    # Create a socket to find an available port
    temp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    temp_socket.bind(('localhost', 0))
    _, port_client = temp_socket.getsockname()
    temp_socket.close()

    # Find an available server port
    temp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    temp_socket.bind(('localhost', 0))
    _, port_server = temp_socket.getsockname()
    temp_socket.close()

    return port_client, port_server


class OSCConfigPanel(bpy.types.Panel):
    bl_label = "OSC Config"
    bl_idname = "VIEW3D_PT_osc_config"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'AutoOSC'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.label(text="IP Address:")
        row.label(text=context.scene.osc_ip_address)

        row = layout.row()
        row.label(text="Client Port:")
        row.label(text=str(context.scene.osc_client_port))

        row = layout.row()
        row.label(text="Server Port:")
        row.label(text=str(context.scene.osc_server_port))

        row = layout.row()
        row.operator("object.get_osc", text="Get OSC")


class OBJECT_OT_GetOSCOperator(bpy.types.Operator):
    bl_label = "Get OSC"
    bl_idname = "object.get_osc"

    def execute(self, context):
        ip_address = socket.gethostbyname(socket.gethostname())
        context.scene.osc_ip_address = ip_address

        client_port, server_port = get_best_ports()
        context.scene.osc_client_port = client_port
        context.scene.osc_server_port = server_port

        self.report({'INFO'}, "OSC IP Address: {}".format(ip_address))
        return {'FINISHED'}


classes = (OSCConfigPanel, OBJECT_OT_GetOSCOperator)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.osc_ip_address = bpy.props.StringProperty(name="OSC IP Address", default="")
    bpy.types.Scene.osc_client_port = bpy.props.IntProperty(name="OSC Client Port", default=0)
    bpy.types.Scene.osc_server_port = bpy.props.IntProperty(name="OSC Server Port", default=0)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.osc_ip_address
    del bpy.types.Scene.osc_client_port
    del bpy.types.Scene.osc_server_port


if __name__ == "__main__":
    register()
