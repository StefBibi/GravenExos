package fr.granvendev.ex;

public class Jouet implements Comparable<Jouet> {

	// attributs
	private String nom;
	private int prix;
	private String description;
	private int promotion;
	
	
	public Jouet() {
		super();
	}
	
	// constructeur
	public Jouet(String nom, int prix, String description, int promotion) {
		super();
		this.nom = nom;
		this.prix = prix;
		this.description = description;
		this.promotion = promotion;
	}
	
	// getters
	public String getNom() {
		return nom;
	}

	public int getPrix() {
		return prix;
	}

	public String getDescription() {
		return description;
	}

	public int getPromotion() {
		return promotion;
	}

	@Override
	public int compareTo(Jouet j2) {
		return this.getNom().compareTo(j2.getNom());
	}	
	
}
