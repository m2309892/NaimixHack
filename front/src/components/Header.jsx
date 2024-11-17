import React from 'react';
import { SvgLogo } from "./Icons";
import './Header.css';  

const Header = () => {
    return (
        <div className="headerAdmin">
            <div className="header-content">
                <div className="left-section">
                    <button>
                        <SvgLogo />
                    </button>
                    <span></span>
                </div>
                <div className="right-section">
                    <button>
                        <img src="../../../../public/admin/message.svg" alt="Message" />
                    </button>
                    <button>
                        <img src="../../../../public/admin/notification.svg" alt="Notification" />
                    </button>
                    <button>
                        <img src="../../../../psublic/admin/Avatar.png" alt="Avatar" />
                    </button>
                    {/* <AddButton/>
                    <NotesButton/>
                    <ModeButton/> */}
                </div>
            </div>
        </div>
    );
}

export default Header;