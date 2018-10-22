package br.com.android;

import com.example.android.market.licensing.R.layout;

import android.app.Activity;
import android.os.Bundle;

public class AppHello extends Activity {
	
	
	@Override
	public void onCreate(Bundle savedInstanceState){
		super.onCreate(savedInstanceState);
		setContentView(layout.main);
	}
}
