class User < ApplicationRecord
  validates :name, length: { maximum: 40 }, presence: true
  validates :email, length: { maximum: 45 }, presence: true
  validates :password, length: { maximum: 45 }, presence: true
end
