import React, { useState, useEffect } from 'react';
import Table from 'react-bootstrap/Table';
import Form from 'react-bootstrap/Form';
import FormControl from 'react-bootstrap/FormControl';
import InputGroup from 'react-bootstrap/InputGroup';
import Device from './Device';
import getDevice from '../endpoints/getDevice';
import getAllDevices from '../endpoints/getAllDevices';

const testData = require('../dummyData.json');

export default function DeviceList() {
    const [deviceList, setDeviceList] = useState([]);
    const [specifiedID, setSpecifiedID] = useState("");

    useEffect(() => {
        if (specifiedID === "") {
            getAllDevices().then(devices => {
                if(devices === undefined) {
                    setDeviceList(testData.devices); // dummy data
                } else {
                    setDeviceList(devices);
                }
            });
        } else {
            updateList();
        }
    });
    
    const updateList = async () => {
        getDevice(specifiedID).then(devices => {
            if(devices === undefined) {
                const deviceArr = testData.devices.filter(device => device.device_id === specifiedID);
                setDeviceList(deviceArr); // dummy data
            } else {
                setDeviceList(devices);
            }
        });
    }

    const handleSearchInput = (e) => {
        setSpecifiedID(e.target.value);
    }

    return (
        <div className="device-table">
            <div className="dashboard-container">
                <h3>Monitored Dispensers</h3>
                <Form
                className="device-search">
                    <InputGroup className="mb-3">
                        <InputGroup.Prepend>
                            <InputGroup.Text>Search by Device ID</InputGroup.Text>
                        </InputGroup.Prepend>
                        <FormControl
                            type="text"
                            placeholder="Enter ID"
                            onChange={handleSearchInput}/>
                    </InputGroup>
                </Form>
            </div>
            <Table bordered>
                <thead>
                    <tr>
                        <th></th>
                        <th>Device ID</th>
                        <th>Location</th>
                        <th>Battery Level</th>
                        <th>Fluid Level</th>
                        <th>Today's Usage</th>
                        <th>Last Maintained</th>
                    </tr>
                </thead>
                <tbody>
                    {deviceList.map((data, index) => <Device deviceData={data} key={index}/>)}
                </tbody>
            </Table>
        </div>
    );
}