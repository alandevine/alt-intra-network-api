import React from 'react';
import MyNavbar from '../components/MyNavbar';

class Settings extends React.Component {
    render () {
        return (
            <div className="settings-page">
                <div className="page-header">
                    <h1>Settings</h1>
                </div>
                <div className="nav-bar">
                    <MyNavbar />
                </div>
                <div className="page-body">
                    <p>To be implemented</p>
                </div>
            </div>
        )
    }
}

export default Settings;