package fr.granvendev.ex;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main1 {
	
	public static void main(String[] args) {

		// creation liste d'objet jouet
		List<String> jouets = new ArrayList<>();
		
		// remplissage liste
        jouets.add("Scrubble Deluxe");
        jouets.add("Jeu avec pleins de roles");
        jouets.add("Zebre Figurine");
        jouets.add("Osobot Evo");
        jouets.add("Araign?e peluche");
        jouets.add("Ligo Start wars");
        jouets.add("Bakogan Battle Pack");
		
		// Affichage : loop from java 8 + lambda
		jouets.stream().forEach(string -> System.out.println(string));
		
		System.out.println("----------------------------------");
		
		// Tri liste alphabetique
		Collections.sort(jouets); // Si liste en String
		
		// Affichage : loop from java 8 + reference
		jouets.forEach(System.out::println); // Si liste en String	
		
	}

}
