package com.practice.ai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AiApplication {

	public static void main(String[] args) {
		System.out.println("debug");
		SpringApplication.run(AiApplication.class, args);
		System.out.println("debug123");
	}

}
