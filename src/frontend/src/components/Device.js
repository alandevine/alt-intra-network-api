import React from 'react';
import Button from 'react-bootstrap/Button';
import '../styles/Dashboard.css';

export default function Device(deviceData) {
    const deviceInfo = deviceData.deviceData;

    const handleViewButton = () => {
        // will display overlay with more detailed info
        console.log("View clicked");
    }

    return (
        <tr key={deviceInfo.device_id}>
            <td className="view-button">
                <Button variant="outline-info" onClick={handleViewButton}>View</Button>
            </td>
            <td>{deviceInfo.device_id}</td>
            <td>{deviceInfo.device_location}</td>
            <td>{(deviceInfo.battery_level * 100)}%</td>
            <td>{(deviceInfo.sanitizer_levels * 100)}%</td>
            <td>N/A</td>
            <td>{deviceInfo.dateLastMaintenance}</td>
        </tr>
    )
}