package fr.granvendev.ex;

import java.util.Comparator;

public class PrixComparator implements Comparator<Jouet> {
	
	@Override
	public int compare(Jouet j1, Jouet j2) {
		if (j1.getPrix() == j2.getPrix()) {
			return j1.compareTo(j2); // Utilisation de l'implement Comparable ajout? a l'objet 
		} else {
//			if (j1.getPrix() > j2.getPrix()) { // version longue
//				return 1;
//			} else {
//				return -1;
//			}
			return j1.getPrix() - j2.getPrix(); // version courte
		}
	}

}
