main_string="""
ScreenManager:
	Home:
	Details:

<Home>:
	name:"mainpage"
	MDBoxLayout:
		size_hint_y:None 
		height:"820dp"
		md_bg_color:(0.2,.2,.2,1)
		orientation:"vertical"
		MDFloatLayout:
			MDLabel:
				text:"Bill App"
				theme_text_color:"Custom"
				text_color:(1,1,1,.8)
				font_style:"Caption"
				font_size:"80dp"
				halign:"center"
				pos_hint:{"center_y":.8}
	MDFloatLayout:
		orientation:"vertical"
		md_bg_color:(1,0,.5,1)
		size_hint:(None,None)
		height:"600dp"
		width:"410dp"
		radius:[150,150,0,0]
		MDTextField:
			id:Quantity
			hint_text:"Enter Quantity of Product. "
			size_hint:None,None
			width:"320dp"
			pos_hint:{"center_y":0.85,"center_x":.5}
			color_mode:"custom"
			text_color:(1,1,1,.8)
			line_color_normal:(1,1,1,.8)
			line_color_focus:(1,1,1,1)
		MDTextField:
			id:Productname
			hint_text:"Enter Product Name."
			size_hint:None,None
			width:"320dp"
			pos_hint:{"center_y":0.75,"center_x":.5}
			color_mode:"custom"
			text_color:(1,1,1,.8)
			line_color_normal:(1,1,1,.8)
			line_color_focus:(1,1,1,1)
		MDTextField:
			id:Cost
			hint_text:"Enter Product Cost."
			normal_color: app.theme_cls.accent_color
    		color_active: 1, 0, 0, 1
			size_hint:None,None
			width:"320dp"
			pos_hint:{"center_y":0.65,"center_x":.5}
			color_mode:"custom"
			text_color:(1,1,1,.8)
			line_color_normal:(1,1,1,.8)
			line_color_focus:(1,1,1,1)
		MDTextField:
			id:Discount
			hint_text:"Enter Discount On Product. "
			size_hint:None,None
			width:"320dp"
			pos_hint:{"center_y":0.55,"center_x":.5}
			color_mode:"custom"
			text_color:(1,1,1,.8)
			line_color_normal:(1,1,1,.8)
			line_color_focus:(1,1,1,1)
		MDRaisedButton:
			text:"Reset"
			theme_text_color:"Custom"
			font_size:"15px"
			md_bg_color:(1,1,1,1)
			pos_hint:{"center_y":0.45,"center_x":.5}
			text_color:(1,0,.7,.8)
			on_release:
				app.erase()
		MDRaisedButton:
			text:"Generate bill"
			theme_text_color:"Custom"
			font_size:"15px"
			md_bg_color:(1,1,1,1)
			pos_hint:{"center_y":0.45,"center_x":.25}
			text_color:(1,0,.7,.8)
			on_release:
				app.details()
				app.change()
				root.manager.current="result_scr"
				app.erase()
	

<Details>:
	name:"result_scr"
	MDBoxLayout:
		size_hint_y:None 
		height:"820dp"
		md_bg_color:(0.2,.2,.2,1)
		orientation:"vertical"
		MDFloatLayout:
			MDLabel:
				text:"Your Result"
				theme_text_color:"Custom"
				text_color:(1,1,1,.8)
				font_style:"Caption"
				font_size:"60dp"
				halign:"center"
				pos_hint:{"center_y":.8}
	MDFloatLayout:
		orientation:"vertical"
		md_bg_color:(1,0,.5,1)
		size_hint:(None,None)
		height:"600dp"
		width:"410dp"
		radius:[150,150,0,0]
		MDLabel:
			id:resPname
			text:"none"
			theme_text_color:"Custom"
			text_color:(1,1,1,.6)
			font_size:"25dp"
			halign:"center"
			pos_hint:{"center_y":.85,"center_x":.5}
		MDLabel:
			id:resPqunatity
			text:"none"
			halign:"center"
			theme_text_color:"Custom"
			text_color:(1,1,1,.6)
			font_size:"25dp"
			pos_hint:{"center_y":.75,"center_x":.5}
		MDLabel:
			id:resCost
			text:"none"
			halign:"center"
			theme_text_color:"Custom"
			text_color:(1,1,1,.6)
			font_size:"25dp"
			pos_hint:{"center_y":.65,"center_x":.5}
		MDLabel:
			id:resDiscount
			text:"none"
			halign:"center"
			theme_text_color:"Custom"
			text_color:(1,1,1,.6)
			font_size:"25dp"
			pos_hint:{"center_y":.55,"center_x":.5}
		MDLabel:
			id:resTotal
			halign:"center"
			text:"none"
			theme_text_color:"Custom"
			text_color:(1,1,1,.6)
			font_size:"20dp"
			pos_hint:{"center_y":.45,"center_x":.5}
		MDRaisedButton:
			text:"Back"
			theme_text_color:"Custom"
			font_size:"15px"
			md_bg_color:(1,1,1,1)
			text_color:(1,0,.7,.8)
			pos_hint:{"center_y":.3,"center_x":.5}
			on_release:
				root.manager.current="mainpage"
	
"""