# [level 2] 상품 별 오프라인 매출 구하기 - 131533 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/131533) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > JOIN

### 채점결과

Empty

### 제출 일자

2025년 08월 03일 00:32:05

### 문제 설명

<p style="user-select: auto !important;">다음은 어느 의류 쇼핑몰에서 판매중인 상품들의 상품 정보를 담은 <code style="user-select: auto !important;">PRODUCT</code> 테이블과 오프라인 상품 판매 정보를 담은 <code style="user-select: auto !important;">OFFLINE_SALE</code> 테이블 입니다. <code style="user-select: auto !important;">PRODUCT</code> 테이블은 아래와 같은 구조로 <code style="user-select: auto !important;">PRODUCT_ID</code>, <code style="user-select: auto !important;">PRODUCT_CODE</code>, <code style="user-select: auto !important;">PRICE</code>는 각각 상품 ID, 상품코드, 판매가를 나타냅니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">Column name</th>
<th style="user-select: auto !important;">Type</th>
<th style="user-select: auto !important;">Nullable</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">PRODUCT_ID</td>
<td style="user-select: auto !important;">INTEGER</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">PRODUCT_CODE</td>
<td style="user-select: auto !important;">VARCHAR(8)</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">PRICE</td>
<td style="user-select: auto !important;">INTEGER</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">상품 별로 중복되지 않는 8자리 상품코드 값을 가지며, 앞 2자리는 카테고리 코드를 의미합니다.</p>

<p style="user-select: auto !important;"><code style="user-select: auto !important;">OFFLINE_SALE</code> 테이블은 아래와 같은 구조로 되어있으며 <code style="user-select: auto !important;">OFFLINE_SALE_ID</code>, <code style="user-select: auto !important;">PRODUCT_ID</code>, <code style="user-select: auto !important;">SALES_AMOUNT</code>, <code style="user-select: auto !important;">SALES_DATE</code>는 각각 오프라인 상품 판매 ID, 상품 ID, 판매량, 판매일을 나타냅니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">Column name</th>
<th style="user-select: auto !important;">Type</th>
<th style="user-select: auto !important;">Nullable</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">OFFLINE_SALE_ID</td>
<td style="user-select: auto !important;">INTEGER</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">PRODUCT_ID</td>
<td style="user-select: auto !important;">INTEGER</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">SALES_AMOUNT</td>
<td style="user-select: auto !important;">INTEGER</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">SALES_DATE</td>
<td style="user-select: auto !important;">DATE</td>
<td style="user-select: auto !important;">FALSE</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">동일한 날짜, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재합니다.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">문제</h5>

<p style="user-select: auto !important;"><code style="user-select: auto !important;">PRODUCT</code> 테이블과 <code style="user-select: auto !important;">OFFLINE_SALE</code> 테이블에서 상품코드 별 매출액(판매가 * 판매량) 합계를 출력하는 SQL문을 작성해주세요. 결과는 매출액을 기준으로 내림차순 정렬해주시고 매출액이 같다면 상품코드를 기준으로 오름차순 정렬해주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">예시</h5>

<p style="user-select: auto !important;">예를 들어 <code style="user-select: auto !important;">PRODUCT</code> 테이블이 다음과 같고 </p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">PRODUCT_ID</th>
<th style="user-select: auto !important;">PRODUCT_CODE</th>
<th style="user-select: auto !important;">PRICE</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">A1000011</td>
<td style="user-select: auto !important;">15000</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">A1000045</td>
<td style="user-select: auto !important;">8000</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">C3000002</td>
<td style="user-select: auto !important;">42000</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;"><code style="user-select: auto !important;">OFFLINE_SALE</code> 테이블이 다음과 같다면</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">OFFLINE_SALE_ID</th>
<th style="user-select: auto !important;">PRODUCT_ID</th>
<th style="user-select: auto !important;">SALES_AMOUNT</th>
<th style="user-select: auto !important;">SALES_DATE</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">2022-02-21</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">2022-03-02</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">2022-05-01</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">2022-05-24</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">5</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">2022-07-14</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">6</td>
<td style="user-select: auto !important;">2</td>
<td style="user-select: auto !important;">1</td>
<td style="user-select: auto !important;">2022-09-22</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto !important;">각 상품 별 총 판매량과 판매가는 다음과 같습니다.</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">PRODUCT_CODE</code> 가 <code style="user-select: auto !important;">A1000011</code>인 상품은 총 판매량이 6개, 판매가가 15,000원</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">PRODUCT_CODE</code> 가 <code style="user-select: auto !important;">A1000045</code>인 상품은 총 판매량이 2개, 판매가가 8,000원</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">PRODUCT_CODE</code> 가 <code style="user-select: auto !important;">C3000002</code>인 상품은 총 판매량이 3개, 판매가가 42,000원</li>
</ul>

<p style="user-select: auto !important;">그러므로 각 상품 별 매출액을 계산하고 정렬하면 결과가 다음과 같이 나와야 합니다.</p>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">PRODUCT_CODE</th>
<th style="user-select: auto !important;">SALES</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">C3000002</td>
<td style="user-select: auto !important;">126000</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">A1000011</td>
<td style="user-select: auto !important;">90000</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">A1000045</td>
<td style="user-select: auto !important;">16000</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges