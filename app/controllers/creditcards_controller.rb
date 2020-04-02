class CreditcardsController < ApplicationController
  before_action :set_creditcard, only: [:show, :edit, :update, :destroy]

  # GET /creditcards
  # GET /creditcards.json
  def index
    @creditcards = Creditcard.all
  end

  # GET /creditcards/1
  # GET /creditcards/1.json
  def show
  end

  # GET /creditcards/new
  def new
    @creditcard = Creditcard.new
  end

  # GET /creditcards/1/edit
  def edit
  end

  # POST /creditcards
  # POST /creditcards.json
  def create
    @creditcard = Creditcard.new(creditcard_params)

    respond_to do |format|
      if @creditcard.save
        format.html { redirect_to @creditcard, notice: 'Creditcard was successfully created.' }
        format.json { render :show, status: :created, location: @creditcard }
      else
        format.html { render :new }
        format.json { render json: @creditcard.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /creditcards/1
  # PATCH/PUT /creditcards/1.json
  def update
    respond_to do |format|
      if @creditcard.update(creditcard_params)
        format.html { redirect_to @creditcard, notice: 'Creditcard was successfully updated.' }
        format.json { render :show, status: :ok, location: @creditcard }
      else
        format.html { render :edit }
        format.json { render json: @creditcard.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /creditcards/1
  # DELETE /creditcards/1.json
  def destroy
    @creditcard.destroy
    respond_to do |format|
      format.html { redirect_to creditcards_url, notice: 'Creditcard was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_creditcard
      @creditcard = Creditcard.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def creditcard_params
      params.require(:creditcard).permit(:network, :cardnumber, :name, :address, :country, :cvv, :exp, :user_id)
    end
end
