package com.strech.notif;

import java.util.Timer;

public class ExecuteSchedule {
	
	  public static void main(String[] args){
		  TrayTimerTask task = new TrayTimerTask();
	      Timer t=new Timer();
	      t.scheduleAtFixedRate(task, 0, 10*60000);

	   }

}