# 📋 NotionLike - Roadmap de développement

## 🏗️ Phase 1 : Structure de base et persistance

### 1.1 Base de données et entités
- [ ] **Configurer la base de données SQLite/PostgreSQL**
  - [ ] Setup des migrations avec Framefox
  - [ ] Configuration de l'ORM (SQLModel/SQLAlchemy)
  - [ ] Tests de connexion DB

- [ ] **Finaliser les relations entre entités**
  - [ ] Relation User ↔ Workspace (1:N)
  - [ ] Relation Workspace ↔ Page (1:N) 
  - [ ] Relation Page ↔ Block (1:N)
  - [ ] Relation Page ↔ Page (hiérarchie parent/enfant)
  - [ ] Index et contraintes de performance

- [ ] **Repositories et Services**
  - [ ] UserRepository avec CRUD complet
  - [ ] WorkspaceRepository avec gestion des permissions
  - [ ] PageRepository avec recherche et hiérarchie
  - [ ] BlockRepository avec sérialisation JSON
  - [ ] Services métier pour la logique complexe

---

## 🔐 Phase 2 : Authentification et sécurité

### 2.1 Système d'authentification
- [ ] **Pages d'authentification**
  - [ ] Page de login avec form validation
  - [ ] Page de register avec confirmation email
  - [ ] Page de mot de passe oublié
  - [ ] Page de profil utilisateur

- [ ] **Backend sécurisé**
  - [ ] Hashage des mots de passe (bcrypt)
  - [ ] JWT tokens pour les sessions
  - [ ] Middleware d'authentification
  - [ ] Gestion des rôles et permissions
  - [ ] Protection CSRF

- [ ] **Frontend sécurisé**
  - [ ] Redirection automatique si non connecté
  - [ ] Gestion des tokens côté client
  - [ ] States de connexion dans l'interface
  - [ ] Logout automatique après expiration

---

## 💾 Phase 3 : Sauvegarde et persistance

### 3.1 Système de sauvegarde en BDD
- [ ] **API REST complète**
  - [ ] CRUD Workspaces (`/api/workspaces/`)
  - [ ] CRUD Pages (`/api/pages/`)
  - [ ] CRUD Blocks (`/api/blocks/`)
  - [ ] Endpoints de recherche et filtrage
  - [ ] Pagination pour les gros datasets

- [ ] **Sauvegarde temps réel**
  - [ ] Auto-save toutes les 2-3 secondes
  - [ ] Détection des conflits de modification
  - [ ] Historique des versions (optionnel)
  - [ ] Sauvegarde hors ligne avec sync (PWA)

- [ ] **Optimisations performance**
  - [ ] Lazy loading des blocs
  - [ ] Cache Redis pour les pages fréquentes
  - [ ] Compression des contenus JSON
  - [ ] Debouncing des requêtes de sauvegarde

---

## 📄 Phase 4 : Gestion des pages et navigation

### 4.1 Système de pages hiérarchiques
- [ ] **Structure arborescente**
  - [ ] Création de pages enfants
  - [ ] Drag & drop pour réorganiser
  - [ ] Breadcrumbs de navigation
  - [ ] Liens internes entre pages

- [ ] **Templates et duplication**
  - [ ] Templates de pages prédéfinis
  - [ ] Duplication de pages existantes
  - [ ] Import/Export de pages (Markdown, JSON)
  - [ ] Conversion Notion → NotionLike

### 4.2 Navigation et workspaces
- [ ] **Interface sidebar**
  - [ ] Liste des workspaces avec switch rapide
  - [ ] Arbre des pages avec expand/collapse
  - [ ] Recherche rapide dans la sidebar
  - [ ] Favoris et pages récentes

- [ ] **Gestion des workspaces**
  - [ ] Création/suppression de workspaces
  - [ ] Partage de workspaces (permissions)
  - [ ] Thèmes et personnalisation par workspace
  - [ ] Statistiques d'utilisation

---

## 📊 Phase 5 : Types de contenu avancés

### 5.1 Tableaux et bases de données
- [ ] **Tableaux simples**
  - [ ] Création de tableaux dans l'éditeur
  - [ ] Ajout/suppression de lignes/colonnes
  - [ ] Types de cellules (texte, nombre, date)
  - [ ] Tri et filtrage basique

- [ ] **Bases de données Notion-like**
  - [ ] Pages en tant que lignes de BDD
  - [ ] Propriétés personnalisées (select, multi-select, etc.)
  - [ ] Vues multiples (tableau, kanban, calendrier)
  - [ ] Formules et rollups
  - [ ] Relations entre bases de données

### 5.2 Nouveaux types de blocs
- [ ] **Blocs de contenu**
  - [ ] Images avec upload et redimensionnement
  - [ ] Vidéos et embeds (YouTube, etc.)
  - [ ] Fichiers attachés avec preview
  - [ ] Code avec coloration syntaxique
  - [ ] Formules mathématiques (LaTeX)

- [ ] **Blocs interactifs**
  - [ ] Todo lists avec cases à cocher
  - [ ] Toggles/accordéons
  - [ ] Callouts colorés
  - [ ] Blocs de citation
  - [ ] Séparateurs et espacements

---

## 🎨 Phase 6 : Interface et expérience utilisateur

### 6.1 Éditeur avancé
- [ ] **Fonctionnalités d'édition**
  - [ ] Sélection multiple de blocs
  - [ ] Copier/coller avec formatage
  - [ ] Undo/Redo avec historique
  - [ ] Raccourcis clavier (Ctrl+B, etc.)
  - [ ] Menu slash (/) avec recherche

- [ ] **Interface responsive**
  - [ ] Adaptation mobile/tablette
  - [ ] Mode sombre/clair
  - [ ] Thèmes personnalisables
  - [ ] Sidebar collapsible

### 6.2 Collaboration (bonus)
- [ ] **Édition collaborative**
  - [ ] WebSockets pour sync temps réel
  - [ ] Curseurs des autres utilisateurs
  - [ ] Commentaires sur les blocs
  - [ ] Notifications de modifications

---

## 🔍 Phase 7 : Fonctionnalités avancées

### 7.1 Recherche et organisation
- [ ] **Recherche globale**
  - [ ] Recherche full-text dans tout le contenu
  - [ ] Filtres par workspace, type, date
  - [ ] Recherche avec preview des résultats
  - [ ] Tags et étiquettes

- [ ] **AI et automatisation**
  - [ ] Suggestions de contenu (IA)
  - [ ] Auto-complétion intelligente
  - [ ] Résumés automatiques de pages
  - [ ] Détection de doublons

### 7.2 Intégrations et API
- [ ] **API publique**
  - [ ] Documentation OpenAPI/Swagger
  - [ ] Webhooks pour les événements
  - [ ] SDK JavaScript/Python
  - [ ] Rate limiting et quotas

- [ ] **Intégrations externes**
  - [ ] Import depuis Notion, Obsidian
  - [ ] Sync avec Google Drive, Dropbox
  - [ ] Intégration Slack/Discord
  - [ ] Export PDF avec mise en page

---

## 🚀 Phase 8 : Performance et déploiement

### 8.1 Optimisations
- [ ] **Performance frontend**
  - [ ] Lazy loading des pages
  - [ ] Virtual scrolling pour gros documents
  - [ ] Service Worker pour cache
  - [ ] Bundle optimization (Vite/Webpack)

- [ ] **Performance backend**
  - [ ] Optimisation des requêtes SQL
  - [ ] Cache distribué (Redis)
  - [ ] CDN pour les assets
  - [ ] Monitoring et métriques

### 8.2 Déploiement et infrastructure
- [ ] **Containerisation**
  - [ ] Dockerfile optimisé
  - [ ] Docker Compose pour développement
  - [ ] Kubernetes manifests (production)
  - [ ] CI/CD avec GitHub Actions

- [ ] **Monitoring et observabilité**
  - [ ] Logs structurés
  - [ ] Métriques applicatives
  - [ ] Alertes automatiques
  - [ ] Backups automatisés

---

## 🎯 Idées de fonctionnalités innovantes

### 💡 Features inspirées d'autres outils
- [ ] **Mode focus** (comme Typora) - écriture sans distraction
- [ ] **Graph view** (comme Obsidian) - visualisation des liens entre pages
- [ ] **Templates dynamiques** - génération de contenu basé sur des variables
- [ ] **Workspaces publics** - partage public de documentation
- [ ] **Mode présentation** - transformation de pages en slides
- [ ] **Calendrier intégré** - planification dans les pages
- [ ] **Pomodoro timer** intégré pour la productivité
- [ ] **Notes vocales** - transcription automatique en texte
- [ ] **Whiteboard/Canvas** - mode tableau blanc pour brainstorming
- [ ] **Système de plugins** - extensions communautaires

### 🔧 Outils de développement et admin
- [ ] **Panel d'administration**
  - [ ] Gestion des utilisateurs
  - [ ] Statistiques d'utilisation
  - [ ] Monitoring des performances
  - [ ] Gestion des sauvegardes

- [ ] **Outils de debugging**
  - [ ] Profiler de requêtes SQL
  - [ ] Timeline des événements
  - [ ] Logs temps réel
  - [ ] Tests de charge automatisés

---

## 📅 Timeline suggérée

**Sprint 1-2 (2-3 semaines)** : Phase 1 + Phase 2
**Sprint 3-4 (2-3 semaines)** : Phase 3 + début Phase 4  
**Sprint 5-6 (2-3 semaines)** : Phase 4 + Phase 5
**Sprint 7-8 (2-3 semaines)** : Phase 6 + optimisations
**Sprint 9+ (évolutif)** : Phases 7-8 + features innovantes

---

*📝 Ce TODO sera mis à jour au fur et à mesure du développement. N'hésitez pas à ajouter vos propres idées !*