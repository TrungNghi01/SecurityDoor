# SecurityDoor

This project is an IoT-based home security solution that uses a Raspberry Pi, motion detector, camera, keypad, RGB LED, and buzzer to secure the entrance to your house. It provides password-based access control, real-time notifications, and logs of entry attempts.

## Features
- motion dectector triggers the system activation
- LED and buzzer change bahvior based on user input (welcome, warning, alert)
- password access via keypad
- servo motor controll the door lock
- automatic picture capture upon access attempt 
- remote picture upload
- admin can fully control the whole system, receive notification for inccorrect password 5 attemps

## components
- **Raspberry Pi** (main controller)
- **Camera** (for capturing images)
- **PIR Motion Sensor** (to detect movement near the door)
- **LED** (visual feedback: green for access granted, red for access denied)
- **Buzzer** (sound feedback: welcome sound for success, warning for failure)
- **Keypad** (for entering the password)
- **Servo Motor** (for controlling door lock)
- **Remote Database** (to store captured images and access logs)
