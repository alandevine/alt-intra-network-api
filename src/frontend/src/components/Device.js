import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import '../styles/Dashboard.css';
// import setDispenseVol from '../endpoints/setDispenseVol';

export default function Device(deviceData) {
    const deviceInfo = deviceData.deviceData;
    const [showDetailedView, setShowDetailedView] = useState(false);

    const handleCloseView = () => {
        setShowDetailedView(false)
    };

    const handleShowView = () => {
        setShowDetailedView(true)
    };

    const handleSaveChanges = () => {
        console.log("Changes saved!");
        handleCloseView();
    }

    return (
        <tr key={deviceInfo.device_id}>
            <td className="view-button">
                <Button variant="outline-info" onClick={handleShowView}>View</Button>
                <Modal
                show={showDetailedView}
                size="lg"
                backdrop="static"
                centered
                onHide={handleCloseView}>
                    <Modal.Header closeButton>
                        <Modal.Title>Dispenser #{deviceInfo.device_id}</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>Adjust indivial dipenser configurations here, e.g. dispense volume.</Modal.Body>
                    <Modal.Footer>
                        <Button variant="primary" onClick={handleSaveChanges}>
                            Save Changes
                        </Button>
                    </Modal.Footer>
                </Modal>
            </td>
            <td className="deviceID-cell">{deviceInfo.device_id}</td>
            <td>{deviceInfo.device_location}</td>
            <td>{(deviceInfo.battery_level * 100)}%</td>
            <td>{(deviceInfo.sanitizer_levels * 100)}%</td>
            <td>N/A</td>
            <td>{deviceInfo.dateLastMaintenance}</td>
        </tr>
    )
}