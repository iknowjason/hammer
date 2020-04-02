class CreateCreditcards < ActiveRecord::Migration[6.0]
  def change
    create_table :creditcards do |t|
      t.string :network
      t.string :cardnumber
      t.string :name
      t.string :address
      t.string :country
      t.integer :cvv
      t.string :exp
      t.integer :user_id

      t.timestamps
    end
  end
end
