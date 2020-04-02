Rails.application.routes.draw do
  resources :creditcards
  resources :users
  root 'dashboard#index'
end
