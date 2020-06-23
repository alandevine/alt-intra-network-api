import React from 'react';
import MyNavbar from '../components/MyNavbar';
import '../styles/Dashboard.css';
import DeviceList from '../components/DeviceList';

class Dashboard extends React.Component {
    render () {
        return (
            <div className="dashboard-page">
                <div className="page-header">
                    <h1>Dashboard</h1>
                </div>
                <div className="nav-bar">
                    <MyNavbar />
                </div>
                <div className="dashboard-body">
                    <DeviceList />
                </div>
            </div>
        )
    }
}

export default Dashboard;