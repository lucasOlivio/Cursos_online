package com.example.android.practiceset2;

import android.support.v7.app.AppCompatActivity;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    int scoreTeamA = 0;

    public void displayForTeamA(int score) {
        TextView scoreView = (TextView) findViewById(R.id.team_a_score);
        scoreView.setText(String.valueOf(score));
    }

    public void pointsThreeTeamA(){
        scoreTeamA += 3;
        displayForTeamA(scoreTeamA);
    }

    public void pointsTwoTeamA(){
        scoreTeamA += 2;
        displayForTeamA(scoreTeamA);
    }

    public void pointsOneTeamA(){
        scoreTeamA += 1;
        displayForTeamA(scoreTeamA);
    }

    int scoreTeamB = 0;

    public void displayForTeamB(int score) {
        TextView scoreView = (TextView) findViewById(R.id.team_a_score);
        scoreView.setText(String.valueOf(score));
    }

    public void pointsThreeTeamB(){
        scoreTeamB += 3;
        displayForTeamB(scoreTeamB);
    }

    public void pointsTwoTeamB(){
        scoreTeamB += 2;
        displayForTeamB(scoreTeamB);
    }

    public void pointsOneTeamB(){
        scoreTeamB += 1;
        displayForTeamB(scoreTeamB);
    }

    public void resetPoints(){
        scoreTeamB = 0;
        displayForTeamB(scoreTeamB);

        scoreTeamA = 0;
        displayForTeamA(scoreTeamA);
    }
}
