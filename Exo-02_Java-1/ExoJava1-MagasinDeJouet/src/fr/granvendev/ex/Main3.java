package fr.granvendev.ex;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main3 {
	
	public static void main(String[] args) {

		// creation liste d'objet jouet
		List<Jouet> jouets = new ArrayList<>();
		
		// remplissage liste
        jouets.add(new Jouet("Scrubble Deluxe", 20, "Petit jeu de société", 5));
        jouets.add(new Jouet("Lu Garu", 15, "Jeu avec pleins de roles", 10));
        jouets.add(new Jouet("Zebre Figurine", 6, "Super figurine de zebre", 5));
        jouets.add(new Jouet("Osobot Evo", 70, "robot pour apprendre à dev", 15));
        jouets.add(new Jouet("Araignée peluche", 30, "peluche toute douce", 5));
        jouets.add(new Jouet("Ligo Start wars", 120, "super ligo box de start wars", 20));
        jouets.add(new Jouet("Bakogan Battle Pack", 20, "jeu de bataille de figurine", 0));
		
		// Affichage
        for(Jouet jouet : jouets) {
            System.out.println("Jouet: " + jouet.getNom() + " ("+ jouet.getPrix() +"€) " +
                    jouet.getDescription() + " (promo: " + jouet.getPromotion() + "% de reduc)");
        }
		
		System.out.println("----------------------------------");
		
		// Tri liste objet
		Collections.sort(jouets,new PrixComparator());
		
        // Afficher la liste à nouveau
        for(Jouet jouet : jouets) {
            System.out.println("Jouet: " + jouet.getNom() + " ("+ jouet.getPrix() +"€) " +
                    jouet.getDescription() + " (promo: " + jouet.getPromotion() + "% de reduc)");
        }		
		
	}

}
