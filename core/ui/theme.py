# Global Style Constants
STYLESHEET = """
    QMainWindow { 
        background-color: #0F0F0F; 
    }
    
    QWidget { 
        color: #F1F1F1; 
        font-family: 'Inter', system-ui, sans-serif; 
    }
    
    #navbar {
        background-color: #1A1A1A;
        border-bottom: 1px solid #333;
        min-height: 65px;
        max-height: 65px;
    }
    
    #sidebar { 
        background-color: #121212; 
        border-right: 1px solid #333; 
        min-width: 250px; 
        max-width: 250px; 
    }
    
    QPushButton#sidebar-item { 
        text-align: left; 
        padding: 16px 25px; 
        background: transparent; 
        color: #AAAAAA; 
        border: none; 
        font-size: 15px;
        font-weight: 500;
    }
    
    QPushButton#sidebar-item:hover { 
        background: #252525; 
        color: #FFFFFF; 
    }
    
    QPushButton#sidebar-item[active="true"] { 
        background: #2D2D2D; 
        color: #3EA6FF; 
        border-left: 4px solid #3EA6FF;
        font-weight: 700;
    }
    
    #nav-action-btn {
        background-color: #2A2A2A;
        color: #FFFFFF;
        border: 1px solid #333;
        border-radius: 20px;
        padding: 0px;
        min-height: 40px;
        max-height: 40px;
        min-width: 40px;
        max-width: 40px;
    }
    
    #nav-action-btn:hover {
        background-color: #333;
        border-color: #3EA6FF;
    }

    /* Page Styles */
    QLabel#page-header {
        font-size: 28px; 
        font-weight: bold; 
        color: #FFFFFF;
    }
    
    QFrame#card {
        background-color: #1A1A1A;
        border: 1px solid #333;
        border-radius: 12px;
        padding: 20px;
    }

    QLineEdit {
        background-color: #121212;
        border: 1px solid #333;
        border-radius: 6px;
        padding: 12px;
        color: #FFFFFF;
        font-size: 14px;
    }
    
    QLineEdit:focus {
        border-color: #3EA6FF;
    }
    
    QPushButton#primary-btn {
        background-color: #3EA6FF;
        color: #0F0F0F;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 800;
    }
    
    QPushButton#primary-btn:hover {
        background-color: #65B8FF;
    }

    QTextEdit#console {
        background-color: #000000;
        border: 1px solid #333;
        border-radius: 10px;
        color: #00FF41;
        font-family: 'Consolas', monospace;
        font-size: 13px;
        padding: 15px;
    }
"""

COLORS = {
    "primary": "#3EA6FF",
    "background": "#0F0F0F",
    "surface": "#1A1A1A",
    "text": "#F1F1F1",
    "text_dim": "#AAAAAA",
    "error": "#CF6679",
    "success": "#03DAC6",
}
