export interface Company {
    id: Number,
    name: String,
    description: String,
    city: String,
    address: String
}
export interface Vacancy {
    id: Number,
    name: String,
    description: String,
    salary: String,
    company_id: Number
}