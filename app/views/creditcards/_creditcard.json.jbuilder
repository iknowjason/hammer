json.extract! creditcard, :id, :network, :cardnumber, :name, :address, :country, :cvv, :exp, :user_id, :created_at, :updated_at
json.url creditcard_url(creditcard, format: :json)
