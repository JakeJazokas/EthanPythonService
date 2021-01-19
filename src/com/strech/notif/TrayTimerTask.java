package com.strech.notif;

import java.awt.AWTException;
import java.awt.SystemTray;
import java.util.TimerTask;

public class TrayTimerTask extends TimerTask {
	
	@Override
	public void run() {
		if (SystemTray.isSupported()) {
            TrayNotificationEvent td = new TrayNotificationEvent();
            try {
				td.displayTray();
			} catch (AWTException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        } else {
            System.err.println("System tray not supported!");
        }
		
	}

}
