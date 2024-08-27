import React, { useState } from 'react';
import axios from 'axios';

const SendNotification = () => {
    const [notification, setNotification] = useState({
        notification_id: '',
        flight_id: '',
        message: '',
        timestamp: '',
        method: '',
        recipient: ''
    });

    const [responseMessage, setResponseMessage] = useState('');
    const [error, setError] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setNotification({ ...notification, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        // Basic form validation
        const { notification_id, flight_id, message, timestamp, method, recipient } = notification;
        if (!notification_id || !flight_id || !message || !timestamp || !method || !recipient) {
            setError('Please fill in all fields.');
            return;
        }

        try {
            const response = await axios.post('http://localhost:5000/send_notification', notification);
            setResponseMessage(response.data.status);
            setError(''); // Clear any previous error
        } catch (error) {
            setError('Error sending notification: ' + error.message);
        }
    };

    return (
        <div className="container">
            <h1>Send Notification</h1>
            <form onSubmit={handleSubmit} className="form">
                <div className="form-group">
                    <label htmlFor="notification_id">Notification ID:</label>
                    <input
                        type="text"
                        id="notification_id"
                        name="notification_id"
                        placeholder="Notification ID"
                        value={notification.notification_id}
                        onChange={handleChange}
                        className="input-field"
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="flight_id">Flight ID:</label>
                    <input
                        type="text"
                        id="flight_id"
                        name="flight_id"
                        placeholder="Flight ID"
                        value={notification.flight_id}
                        onChange={handleChange}
                        className="input-field"
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="message">Message:</label>
                    <input
                        type="text"
                        id="message"
                        name="message"
                        placeholder="Message"
                        value={notification.message}
                        onChange={handleChange}
                        className="input-field"
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="timestamp">Timestamp:</label>
                    <input
                        type="datetime-local"
                        id="timestamp"
                        name="timestamp"
                        value={notification.timestamp}
                        onChange={handleChange}
                        className="input-field"
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="method">Method (SMS, Email, App):</label>
                    <select
                        id="method"
                        name="method"
                        value={notification.method}
                        onChange={handleChange}
                        className="input-field"
                    >
                        <option value="">Select Method</option>
                        <option value="SMS">SMS</option>
                        <option value="Email">Email</option>
                        <option value="App">App</option>
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="recipient">Recipient:</label>
                    <input
                        type="text"
                        id="recipient"
                        name="recipient"
                        placeholder="Recipient"
                        value={notification.recipient}
                        onChange={handleChange}
                        className="input-field"
                    />
                </div>
                <button type="submit" className="submit-button">Send Notification</button>
            </form>

            {error && <p className="error-message">{error}</p>}
            {responseMessage && <p className="success-message">{responseMessage}</p>}
        </div>
    );
};

export default SendNotification;
